import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from threading import Thread, Lock
import requests
from datetime import datetime, timedelta

# Importar db de models para evitar importação circular
from models import db, User, Post

mail = Mail()
login_manager = LoginManager()
quote_cache = {'text': None, 'author': None, 'fetched_at': None}
quote_lock = Lock()

# Configurar user_loader aqui
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-key'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL', 'sqlite:///app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MAIL_SERVER=os.environ.get('MAIL_SERVER', 'smtp.example.com'),
        MAIL_PORT=int(os.environ.get('MAIL_PORT', 587)),
        MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
        MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
        MAIL_USE_TLS=bool(int(os.environ.get('MAIL_USE_TLS') or 0)),
        MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER', 'no-reply@example.com')
    )

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from forms import LoginForm, RegistrationForm, PostForm, ProfileForm
    from email_utils import send_confirmation_email, confirm_token

    @app.before_request
    def ensure_quote_background():
        # Ensure there is an initial async fetch of quote (only run once)
        if not hasattr(app, '_quote_started'):
            app._quote_started = True
            # Only try to fetch quote if we don't have one or it's older than 1 hour
            with quote_lock:
                should_fetch = (quote_cache['text'] is None or 
                              quote_cache['fetched_at'] is None or 
                              (datetime.utcnow() - quote_cache['fetched_at']).total_seconds() > 3600)
            if should_fetch:
                def starter():
                    with app.app_context():
                        fetch_and_translate_quote(app)
                Thread(target=starter, daemon=True).start()

    @app.route('/')
    def index():
        posts = Post.query.order_by(Post.created_at.desc()).all()
        return render_template('index.html', posts=posts)

    @app.route('/quote_status')
    def quote_status():
        # Return current quote if available
        with quote_lock:
            if quote_cache['text']:
                return jsonify({
                    'text': quote_cache['text'],
                    'author': quote_cache['author'],
                    'fetched_at': quote_cache['fetched_at'].isoformat() if quote_cache['fetched_at'] else None
                })
            else:
                return jsonify({}), 204

    @app.route('/trigger_fetch_quote')
    def trigger_fetch_quote():
        # Start background thread to fetch quote (non-blocking)
        Thread(target=fetch_and_translate_quote, args=(app,), daemon=True).start()
        return jsonify({'status':'started'})

    @app.route('/register', methods=['GET','POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            from sqlalchemy.exc import IntegrityError
            
            # Check if username or email already exists
            existing_user = User.query.filter_by(username=form.username.data).first()
            if existing_user:
                flash('Nome de usuário já existe. Escolha outro.', 'danger')
                return render_template('register.html', form=form)
                
            existing_email = User.query.filter_by(email=form.email.data).first()
            if existing_email:
                flash('Email já está registrado. Use outro email ou faça login.', 'danger')
                return render_template('register.html', form=form)
            
            # Create new user
            u = User(username=form.username.data, email=form.email.data)
            u.set_password(form.password.data)
            
            # Check if we're in development mode (no real email server)
            is_dev_mode = (app.config.get('MAIL_SERVER') == 'smtp.example.com' or 
                          os.environ.get('FLASK_ENV') == 'development')
            
            try:
                if is_dev_mode:
                    # In development, auto-confirm the user
                    u.confirmed = True
                    db.session.add(u); db.session.commit()
                    flash('Conta criada e ativada automaticamente (modo desenvolvimento)!', 'success')
                else:
                    # In production, send confirmation email
                    db.session.add(u); db.session.commit()
                    try:
                        token = send_confirmation_email(u, app, mail)
                        flash('Conta criada! Verifique seu email para ativar a conta.', 'info')
                    except Exception as e:
                        app.logger.error(f'Erro ao enviar email de confirmação: {e}')
                        # Fallback: auto-confirm if email fails
                        u.confirmed = True
                        db.session.commit()
                        flash('Conta criada e ativada automaticamente (email indisponível)!', 'warning')
                
                return redirect(url_for('login'))
                
            except IntegrityError:
                db.session.rollback()
                flash('Erro ao criar conta. Nome de usuário ou email já podem estar em uso.', 'danger')
                return render_template('register.html', form=form)
            
        return render_template('register.html', form=form)

    @app.route('/confirm/<token>')
    def confirm_email(token):
        try:
            email = confirm_token(token, app)
        except Exception as e:
            flash('Token inválido ou expirado.', 'danger')
            return redirect(url_for('index'))
        user = User.query.filter_by(email=email).first_or_404()
        user.confirmed = True
        db.session.commit()
        flash('Email confirmado! Agora você pode fazer login.', 'success')
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET','POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            u = User.query.filter_by(email=form.email.data).first()
            if u and u.check_password(form.password.data) and u.confirmed:
                login_user(u, remember=form.remember.data)
                return redirect(url_for('index'))
            flash('Credenciais inválidas ou conta não confirmada.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/post/new', methods=['GET','POST'])
    @login_required
    def create_post():
        form = PostForm()
        if form.validate_on_submit():
            p = Post(title=form.title.data, body=form.body.data, author_id=current_user.id)
            db.session.add(p); db.session.commit()
            flash('Post criado.', 'success')
            return redirect(url_for('index'))
        return render_template('create_post.html', form=form)

    @app.route('/post/<int:post_id>')
    def post_detail(post_id):
        p = Post.query.get_or_404(post_id)
        return render_template('post_detail.html', post=p)

    @app.route('/post/<int:post_id>/edit', methods=['GET','POST'])
    @login_required
    def edit_post(post_id):
        p = Post.query.get_or_404(post_id)
        if not (current_user.id == p.author_id or current_user.role in ('moderator','admin')):
            flash('Permissão negada.', 'danger'); return redirect(url_for('index'))
        form = PostForm(obj=p)
        if form.validate_on_submit():
            p.title = form.title.data; p.body = form.body.data; db.session.commit()
            flash('Post atualizado.', 'success'); return redirect(url_for('post_detail', post_id=p.id))
        return render_template('edit_post.html', form=form, post=p)

    @app.route('/post/<int:post_id>/delete', methods=['POST'])
    @login_required
    def delete_post(post_id):
        p = Post.query.get_or_404(post_id)
        if not (current_user.id == p.author_id or current_user.role in ('moderator','admin')):
            flash('Permissão negada.', 'danger'); return redirect(url_for('index'))
        db.session.delete(p); db.session.commit()
        flash('Post excluído.', 'success'); return redirect(url_for('index'))

    @app.route('/perfil', methods=['GET','POST'])
    @login_required
    def perfil():
        form = ProfileForm(obj=current_user)
        if form.validate_on_submit():
            current_user.username = form.username.data
            db.session.commit()
            flash('Perfil atualizado.', 'success')
        return render_template('profile.html', form=form)

    @app.route('/admin/users', methods=['GET','POST'])
    @login_required
    def admin_users():
        if current_user.role != 'admin':
            flash('Acesso negado.', 'danger'); return redirect(url_for('index'))
        users = User.query.all()
        if request.method == 'POST':
            uid = int(request.form.get('user_id')); new_role = request.form.get('role')
            u = User.query.get(uid); u.role = new_role; db.session.commit(); flash('Papel atualizado.', 'success')
        return render_template('admin_users.html', users=users)

    return app

def fetch_and_translate_quote(app):
    """Fetch a random quote from Quotable and translate it to Portuguese using a translation API.
    This function is designed to be run in a background thread (non-blocking).
    """
    with app.app_context():
        try:
            r = requests.get('https://api.quotable.io/random', timeout=5)
            if r.status_code == 200:
                data = r.json()
                text = data.get('content')
                author = data.get('author')
                # Translate (example using LibreTranslate public instance)
                try:
                    t = requests.post('https://libretranslate.de/translate', json={
                        'q': text,
                        'source': 'en',
                        'target': 'pt'
                    }, timeout=8)
                    if t.status_code == 200:
                        translated = t.json().get('translatedText')
                    else:
                        translated = text  # fallback
                except Exception:
                    translated = text
                with quote_lock:
                    quote_cache['text'] = translated
                    quote_cache['author'] = author
                    quote_cache['fetched_at'] = datetime.utcnow()
            else:
                # Provide a fallback quote when API is not available
                with quote_lock:
                    quote_cache['text'] = "A jornada de mil milhas começa com um único passo."
                    quote_cache['author'] = "Lao Tzu"
                    quote_cache['fetched_at'] = datetime.utcnow()
        except Exception as e:
            # Provide a fallback quote and log only once per hour
            with quote_lock:
                if (quote_cache.get('last_error_logged') is None or 
                    (datetime.utcnow() - quote_cache.get('last_error_logged', datetime.min)).total_seconds() > 3600):
                    app.logger.warning('API de citações indisponível, usando citação padrão. Erro: %s', str(e))
                    quote_cache['last_error_logged'] = datetime.utcnow()
                quote_cache['text'] = "O sucesso é a soma de pequenos esforços repetidos dia após dia."
                quote_cache['author'] = "Robert Collier"
                quote_cache['fetched_at'] = datetime.utcnow()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

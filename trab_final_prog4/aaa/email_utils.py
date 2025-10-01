from itsdangerous import URLSafeTimedSerializer
from flask import url_for
from flask_mail import Message
import os

def generate_serializer(app):
    return URLSafeTimedSerializer(app.config['SECRET_KEY'])

def send_confirmation_email(user, app, mail):
    s = generate_serializer(app)
    token = s.dumps(user.email, salt='email-confirm')
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = f'<p>Olá {user.username},</p><p>Por favor confirme sua conta clicando no link: <a href="{confirm_url}">Confirmar email</a></p>'
    msg = Message('Confirme sua conta', recipients=[user.email], html=html)
    mail.send(msg)
    return token

def confirm_token(token, app, expiration=3600):
    s = generate_serializer(app)
    email = s.loads(token, salt='email-confirm', max_age=expiration)
    return email

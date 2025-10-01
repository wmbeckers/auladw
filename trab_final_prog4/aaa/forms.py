from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(3,80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6,128)])
    password2 = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(1,200)])
    body = TextAreaField('Conteúdo', validators=[DataRequired(), Length(1,10000)])
    submit = SubmitField('Salvar')

class ProfileForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(3,80)])
    submit = SubmitField('Atualizar')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField,SubmitField,IntegerField


class LoginForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')


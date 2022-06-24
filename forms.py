from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, length, Email, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from app import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), length(min=2, max=20)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

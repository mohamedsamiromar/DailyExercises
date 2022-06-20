from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, length, Email


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), length(min=2, max=20)])
    submit = SubmitField('Sign Up')
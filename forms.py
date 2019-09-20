from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField # , TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, message='Se requieren mínimo tres caracteres')])
    submit = SubmitField('Login')
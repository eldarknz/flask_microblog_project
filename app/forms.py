from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username    = StringField('Username', render_kw={"placeholder": "Enter your username"}, validators=[DataRequired()])
    password    = PasswordField('Password', render_kw={"placeholder": "Enter your password"}, validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username  = StringField('Username', render_kw={"placeholder": "Enter your username"}, validators=[DataRequired()])
    email     = StringField('Email Address', render_kw={"placeholder": "name@address.com"}, validators=[DataRequired(), Email()])
    password  = PasswordField('Password', render_kw={"placeholder": "Enter your password"}, validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', render_kw={"placeholder": "Repeat your password"}, validators=[DataRequired(), EqualTo('password')])
    submit    = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

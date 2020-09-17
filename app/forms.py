from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password_one = PasswordField('Password', validators=[DataRequired()])
    password_two = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password_one')])
    submit = SubmitField('Register')

    # Making sure that the entered username not already in the database.
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please try a different username.')

    # Making sure that the entered email not already in the database.
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please try a different email address.')


class PostCreationForm(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Content')
    submit = SubmitField('Create')


class AnalyticsForm(FlaskForm):
    date_from = StringField('Date from:', validators=[DataRequired()])
    date_to = StringField('Date to:', validators=[DataRequired()])
    submit = SubmitField('Analyse')
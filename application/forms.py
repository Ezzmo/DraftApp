from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import *
from flask_login import current_user

class ChooseForm(FlaskForm):

    name = StringField('Name your team',
            validators = [
                DataRequired(),
                Length(min=3, max=100)
            ]
    )

    player1 = StringField('LW',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    player2 = StringField('RW',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    player3 = StringField('ST',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    player4 = StringField('RB',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    player5 = StringField('LB',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    def validate_name(self, name):
        name = Userteams.query.filter_by(teamname=name.data).first()

        if name:
            raise ValidationError('Name already in use')

    submit = SubmitField('Post team')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired(),
		])
	remember = BooleanField('Remember Me')
    
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
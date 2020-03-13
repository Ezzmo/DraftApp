from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
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

    player1 = SelectField('Player 1', choices=[])
    player2 = SelectField('Player 2', choices=[])
    player3 = SelectField('Player 3', choices=[])
    player4 = SelectField('Player 4', choices=[])
    player5 = SelectField('Player 5', choices=[])


    def validate_name(self, name):
        name = Userteams.query.filter_by(teamname=name.data).first()

        if name:
            raise ValidationError('Name already in use')

    submit = SubmitField('Post team')

class RegistrationForm(FlaskForm):
    name = StringField('Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
    )

    age = StringField('Age',
            validators = [
                DataRequired(),
            ]
    )
    position = StringField('Position',
            validators = [
                DataRequired()
            ]
    )
    submit = SubmitField('Sign Up')

    def validate_name(self, name):
        user = Players.query.filter_by(name=name.data).first()

        if user:
            raise ValidationError('Name already in database')


class LoginForm(FlaskForm):
	name = StringField('Name',
		validators=[
			DataRequired(),
		])
	password = PasswordField('Password',
		validators=[
			DataRequired(),
		])
	remember = BooleanField('Remember Me')
    
	submit = SubmitField('Login')

class UpdateTeamForm(FlaskForm):
    name = StringField('Team Name/Week',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )
    player1 = SelectField('Player 1', choices=[])
    player2 = SelectField('Player 2', choices=[])
    player3 = SelectField('Player 3', choices=[])
    player4 = SelectField('Player 4', choices=[])
    player5 = SelectField('Player 5', choices=[])

    update = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
    
    


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from models import User, DinnerParty

# registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# dinner party form
class DinnerPartyForm(FlaskForm):
    date = StringField('Date', validators = [DataRequired()])
    venue = StringField('Venue', validators = [DataRequired()])
    main_dish = StringField('Dish', validators = [DataRequired()])
    number_seats = StringField('Number of Seats')
    submit = SubmitField('Create')

# rsvp form
class RsvpForm(FlaskForm):
    party_id = StringField('Party ID', validators = [DataRequired()])
    submit = SubmitField('RSVP')

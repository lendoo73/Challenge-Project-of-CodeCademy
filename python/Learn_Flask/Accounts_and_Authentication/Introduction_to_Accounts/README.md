# Introduction to Accounts

## [Intro to Accounts with Flask](https://www.codecademy.com/courses/learn-flask/lessons/flask-accounts/exercises/intro-to-accounts-with-flask)

Accounts are the end result of gathering data necessary to create a user for a website. 
They also allow you to keep logging in to use the application.

By the end of this lesson you will be familiar with the concepts and code necessary to create a web application with user account functionality.

Remember Flask is a micro-framework with web server functionality and built in tools to make web development simple and enjoyable. 
Along the way we will use other Flask tools to address our development needs.

We will be using Flask’s Flask-Login, SQLAlchemy and WTForms Python packages to build our application. 
The application will allow you to invite your friends to a dinner party, and users will have the power to login and RSVP for the fun evening.

## [Introduction to Hashing](https://www.codecademy.com/courses/learn-flask/lessons/flask-accounts/exercises/intro-to-hashing)

An important rule of application development is to **never store sensitive user data as plain text**. 
Plain text data is a security risk, as a data breach or hack would allow sensitive data to fall into the wrong hands.

How can we store sensitive user data, such as passwords, in a more secure format? 
Step in hashing! 
Hashing is the process of taking text input and creating a new sequence of characters out of it that cannot be easily reverse-engineered.

When we hash user passwords, we can store the hashed format rather than the original plain text passwords. 
If a hack were to occur, the hackers would not be able to exploit the stolen information without knowing the hashing function that was used to encrypt the data.

We can add hashing functionality to a Flask application using the security module of the Werkzeug package.

To hash a password:
```
hashed_password = generate_password_hash("noONEwillEVERguessTHIS")
```
* `generate_password_hash()` takes a string as an argument and returns a hash of the string

We can also check a user-entered password against our hashed password to check for a match:
```
hash_match = check_password_hash(hashed_password, "IloveTHEcolorPURPLE123")
print(hash_match) # will print False 
hash_match = check_password_hash(hashed_password, "noONEwillEVERguessTHIS")
print(hash_match) # will print True 
```
* `check_password_hash()` takes two arguments: 
  * the hashed string 
  * and a new string 
which we are checking the hash against. 
* It returns a boolean indicating if the string was a match to the hash.

## [Modeling Accounts w/ SQLAlchemy](https://www.codecademy.com/courses/learn-flask/lessons/flask-accounts/exercises/modeling-accounts-wsqlalchemy)

When creating a user account in an application, there are a variety of data that needs to be stored for each user, as well as associated methods. 
The best way to store this data for a Flask application is as a model in a database managed by Flask-SQLAlchemy.

There are some fields we might want to store for each of our users no matter what kind of application we are creating. 
For example, these fields can include: **`id`**, **`username`**, **`email`**, **`password_hash`**, and **`joined_at_date`**. 
A good way to store this data is in a User model within your database. 
For example, given some database `db`:
```
class User (db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(64), index = True, unique = True)
  email = db.Column(db.String(120), index = True, unique = True)
  password_hash = db.Column(db.String(128))
  joined_at_date = db.Column(db.DateTime(), index = True, default = datetime.utcnow)
```
* here we instantiate a model `User`
* that stores primary key `id` as an `Integer`
* `username`, `email` and `password_hash` as `String`s, and
* `joined_at_date` as a `DateTime`

In addition to this informational data, we want to add methods that represent different user needs. 
We could write these methods ourselves, but Flask-Login does that work for us with the help of mixins. 
Mixins help us inject some standard code into a class to make life easier. 
In this case, we will inherit the methods and properties of the `UserMixin` class.
```
from flask_login import UserMixin
 
class User(UserMixin, db.Model)
```
* when we inherit from UserMixin, we inherit some of the following functions: `is_active()`, `is_authenticated()`, `is_anonymous()`
* these functions will be helpful later on for understanding the state of our users

## [Signing up with WTForms](https://www.codecademy.com/courses/learn-flask/lessons/flask-accounts/exercises/signing-up-with-wtforms)

Now that we’ve got a database setup, our dinner application is starting to take shape. 
We’re going to need to get some data from our friends in order to make their dinner party accounts.

We could get all kinds of juicy information from them like their favorite dish or favorite chef, but for now, we’ll just grab their email address, username, and password. 
To get this information we’ll need to provide the user with an interface that has input areas for the respective fields that need to be filled out. 
An HTML form is a perfect way to gather this data!

We will use WTForms to create forms that make it easy for us to grab the data we need.
```
class RegistrationForm(FlaskForm):
  username = StringField('Username', validators = [DataRequired()])
  email = StringField('Email', validators = [DataRequired(), Email()])
  password = PasswordField('Password', validators = [DataRequired()])
  password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')
```
* a class `RegistrationForm` is defined and inherits from `FlaskForm`
* `StringField`s `username` and `email` are defined with the appropriate validators
* `PasswordField`s `password` and `password2` are defined with the appropriate validators to ensure the same password is entered twice
* a `SubmitField` named `submit` is defined

And we will have a route that allows the users to create an account.
```
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(
      username = form.username.data, 
      email = form.email.data
    )
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', form = form)
```
* a `RegistrationForm` named `form` is created
* if the form is validated upon submission, a `User` named `user` is created with a `username` and `email` from the form data
* the `user`‘s password is set and hashed using the `set_password` method
* the `user` is added to the database session and the session is committed

Lastly, we need to make sure to update our template file to make sure the form is displayed properly to our users.

## [Login in with Flask](https://www.codecademy.com/courses/learn-flask/lessons/flask-accounts/exercises/logging-in-with-flask-login)









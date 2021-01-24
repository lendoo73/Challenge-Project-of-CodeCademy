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

We currently have a working form grabbing user data and signing them up to our application. 
Next, let’s allow users to login by using a Flask-Login object called `LoginManager()`.
```
login_manager = LoginManager()
login_manager.init_app(app)
```
* here we create a `LoginManager` object and initialize it with the `init_app()` method and our application object `app`

Flask-Login provides us with a helpful decorator that we’ll place on endpoints we want to be protected. 
Remember, decorators allow us to run bits of code before ultimately running a function or in this case our flask endpoint.
```
@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username = username).first_or_404()
  return render_template('user.html', user = user)
```
* the `@login_required` decorator is used to protect the `user` route
* the `User` table is queried for a user that matches the provided username

We will use this decorator on every Flask endpoint that we want only accessible by logged in users. 
This will check to make sure the user login is still stored in memory. 
So long as the user memory has not been cleared with a logout or browser refreshing clear, the `LoginManager()` will be able to retrieve the identity of the user before allowing them to access the information on that page.

We also need an additional helper function to load our individual user when trying to access protected routes.
```
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```
* the `load_user()` function loads a user with a given `user_id`

We can then login a user with a login route, paired with a login form, as shown below:
```
@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm(csrf_enabled = False)
  if form.validate_on_submit():
    user = User.query.filter_by(email = form.email.data).first()
    if user and user.check_password(form.password.data):
      login_user(user, remember = form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('index', _external = True, _scheme = 'https'))
    else:
      return redirect(url_for('login', _external = True, _scheme = 'https'))
  return render_template('login.html', form = form)
```
* initialize a `LoginForm` `form`
* if the form validates, query the `User` table for the user with an email that matches the provided email
* if a user is found `user.check_password(form.password.data)` checks the form entered password against the user’s password
* if there is a match, `login_user()` logs `user` in and redirects to either `next_page` or the index route
* if no user is found or the password does not match, we redirect to the login route

## [Associating User Actions](https://www.codecademy.com/courses/learn-flask/lessons/flask-accounts/exercises/ensuring-user-action-integrity)

Our users are now able to create accounts and log in. 
You may be curious, and ask yourself, “How can I make sure that they manipulate only their data and not someone else’s?”

We solve this association problem by making every dinner party an instance of a `DinnerParty` model, where each party is created by an instance of the `User` model. 
We can then use the unique identifying attributes of each object to ensure functionality like creating new dinner parties hosted by a specific user and letting users RSVP to a specific dinner party.

We can update our user endpoint with functionality to check for existing dinner parties and create a new dinner party using a form:
```
def user(username):
  user = User.query.filter_by(username = username).first_or_404()
  dinner_parties = DinnerParty.query.filter_by(party_host_id = user.id)
  if dinner_parties is None:
    dinner_parties = []
  form = DinnerPartyForm(csrf_enabled = False)
```
* query the `DinnerParty` model for all dinner parties where the party host is our logged-in user, and store the parties in `dinner_parties`
* if there is no dinner party hosted by the logged-in user, set `dinner_parties` to an empty list
* create a `DinnerPartyForm` named `form`

Once the user submits the form for a new dinner party, we can use the form data to create a new `DinnerParty` instance:
```
  # user route continued
  if form.validate_on_submit():
    new_dinner_party = DinnerParty(
      date = form.date.data,
      venue = form.venue.data,
      main_dish = form.main_dish.data,
      number_seats = int(form.number_seats.data), 
      party_host_id = user.id,
      attendees = username)
    db.session.add(new_dinner_party)
    db.session.commit()
  return render_template('user.html', user = user, dinner_parties = dinner_parties, form = form)
```
* if `form` validates, create a new `DinnerParty` object `new_dinner_party`
* the `DinnerParty` attributes (`date`, `venue`, …, `attendees`) are assigned values from their accompanying form field data
* the `attendees` attribute is initialized with the logged-in user’s `username`
* `new_dinner_party` is added to the session and committed

We can create a new route that will allow users to see all the dinner parties that are happening and provide a form for RSVPing to a specific party:
```
def rsvp(username):
  user = User.query.filter_by(username = username).first_or_404()
  dinner_parties = DinnerParty.query.all()
  if dinner_parties is None:
    dinner_parties = []
  form = RsvpForm(csrf_enabled = False)
  if form.validate_on_submit():
    dinner_party = DinnerParty.query.filter_by(id = int(form.party_id.data)).first()
    dinner_party.attendees += f", {username}"
    db.session.commit()
  return render_template('rsvp.html', user = user, dinner_parties = dinner_parties, form = form)
```
* set `user` to the logged-in user
* query all dinner parties in the `DinnerParty` model and save them to `dinner_parties` for display on the page
* create an RSVP form named `form`
* if `form` validates, query the `DinnerParty` model for the dinner party with an `id` that matches the `id` entered in the form
* update the attendee list with the logged-in user’s `username` and commit the change

## [Success and Error Handling](https://www.codecademy.com/courses/learn-flask/lessons/flask-accounts/exercises/success-and-error-handling-with-flask-flash)

As we round things up, it’s a good idea to make sure the user experience is thoughtful by implementing a way to notify the user when an RSVP succeeds or if they need to try again in case an error occurs.

Flask provides us with the `flash()` method to communicate messages powered by the backend. 
With flash, Flask can record a message at the end of a request and access it on the next request only. 
We can thus use flash to notify users whether their important actions succeed or fail.

Consider the second half of the RSVP route from the previous exercise. 
We can update our code to better notify users of what occurs as follows:
```
# second half of rsvp route
  if form.validate_on_submit():
    dinner_party = DinnerParty.query.filter_by(id = int(form.party_id.data)).first()
    # new try block
    try:
      dinner_party.attendees += f", {username}"
      db.session.commit()
      # find the host of dinner_party
      host = User.query.filter_by(id = int(dinner_party.party_host_id)).first()
      flash(f"You successfully RSVP'd to {host.username}'s dinner party on {dinner_party.date}!")
    # new except block
    except:
      flash("Please enter a valid Party ID to RSVP!")
  return render_template('rsvp.html', user = user, dinner_parties = dinner_parties, form = form)
```
* the update to `dinner_party.attendees` and the commit now occur inside a try block
* the `User` model is queried for the user hosting `dinner_party` and stored in `host`
* inside the `try` block, `flash()` is given a string message as an argument to notify the user that an RSVP successfully occurred
* an `except` block is called when there is an error RSVP’ing
* inside the `except` block, `flash()` is given a string message as an argument to notify the user that they were not able to RSVP successfully

With the route updated, we can access our flashed messages in a template file and display them on our page as follows:
```
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      {{ message }}
    {% endfor %}
  {% endif %}
{% endwith %}
```
* the `get_flashed_messages()` function returns all flashed messages in the last session and saves the messages to `messages`
* `if` there are any messages, we `for` loop through each `message` in `messages` and display the message `{{ message }}`

It’s best practice to look at your code and evaluate areas where things can go wrong. 
When you identify these points, you can utilize `flash()` to provide feedback to the user on what exactly happened and how they can proceed.

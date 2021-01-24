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









While we are hardcoding our passwords here, in later exercises we will see how to collect this information using a Form.

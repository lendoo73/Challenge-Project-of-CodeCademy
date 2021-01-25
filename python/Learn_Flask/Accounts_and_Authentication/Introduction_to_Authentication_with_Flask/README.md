# Introduction to Authentication with Flask

## [Intro to Authentication](https://www.codecademy.com/courses/learn-flask/lessons/flask-authentication/exercises/intro-to-authentication)

Authentication is the process of verifying that an individual has permission to perform an action. 
Without authentication, there would be no way of knowing or enforcing access control on our browser for our applications.

Our strategy of authenticating users depends on discerning whether a password is valid or not in order to allow the user to perform further actions in the application.

In the next lesson we’ll get to know some of the tools that we can use to authenticate in Python Flask applications by building a 
web application that allows authenticated users to view an awesome secret recipe.

## [Meet Flask-Login](https://www.codecademy.com/courses/learn-flask/lessons/flask-authentication/exercises/using-flask-login-to-protect-pages)

When building a web application we might first start with the base of our application serving an endpoint saying “Hello World”.
```
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello Authentication World!'
```
The application we will be building will show how to use tools in Flask to authenticate users. 
The primary tool we can use to achieve our purposes of authenticating in Flask is [Flask-Login](https://flask-login.readthedocs.io/en/latest/).

Flask-Login is a third-party package that allows us to use pieces of code that enable us to perform authentication actions in our application.

We can manage user logins with the `LoginManager` object from within Flask-Login, as shown below:
```
from flask_login import LoginManager
 
login_manager = LoginManager()
```
* `LoginManager` is imported from the `flask_login` package
* a new `LoginManager` object named `login_manager` is created

Once a `LoginManager` object is defined, we need to initialize the manager with our application. 
This can be done with the `init_app()` method of a `LoginManager`:
```
login_manager.init_app(app)  
```
* our instance of `LoginManager`, `login_manager`, calls its `init_app()` method with `app`, an initialized Flask app, as an argument

## [Protecting Pages](https://www.codecademy.com/courses/learn-flask/lessons/flask-authentication/exercises/requiring-login-before-viewing)

Protecting pages is the primary objective of authentication. 
We can leverage some very useful functions from Flask-Login to ensure our different pages or routes are protected.

One of the key pieces of code that we previously added is the `LoginManager` object that we initialized with our instance of the Flask application. 
`LoginManager` have a method `user_loader` that needs to be defined in order to load and verify a user from our database.
```
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
```
* this method retrieves our `User` with an id value `id` from our database
* without this function, we won’t be able to verify users on our protected routes!

Next we need to import the `login_required` function from `flask_login` at the top of our file:
```
from flask_login import login_required
```
We can now add the `@login_required` function as a decorator to different routes to make logging in necessary.
```
@app.route('/home')
@login_required
def home():
    return render_template('logged_in.html')
```
The `@login_required` decorator will force the user to login before being able to view the page.

## [Error Handling](https://www.codecademy.com/courses/learn-flask/lessons/flask-authentication/exercises/error-handling-and-communicating-to-the-user)

We’ve all experienced a time when we thought we were logged into a site and tried to access a protected page. 
Some sites handle this better than others, by letting the user know that the requested page is only for authenticated users.

When our user tries to access protected pages without logging in or encounters an error upon login, its best we communicate this somehow to the user.

We can catch authorization issues by adding a new route or endpoint with the `@login_manager.unauthorized_handler` decorator:
```
@login_manager.unauthorized_handler
def unauthorized():
  # do stuff
  return "Sorry you must be logged in to view this page"
```
* the `@login_manager.unauthorized_handler` decorator ensures that any time there is an authorization issue, the `unauthorized()` route is called
* the message in the `return` statement is HTML that is served to non-authenticated users. 
We can replace this with a template that users who fail to login see.

## [Logging in a User](https://www.codecademy.com/courses/learn-flask/lessons/flask-authentication/exercises/logging-in-a-user)

Best practices for user authentication using Flask is to make it hard for someone to use a stolen credential.

To achieve this in Flask use the Flask’s Werkzeug library which has `generate_password_hash` method to generate a hash, and `check_password_hash` method to compare login input with the value returned from the `check_password_hash` method.

Our login code will check whether the value passed in is the same as the hardcoded user we are using to emulate a database.

We create a `User` class to represent a user. 
This object takes advantage of `UserMixin` (Mixins are prepackaged code of common code needs). 
In this case we use `UserMixin` because it allows us to take advantage of common user account functions without having to write it all ourselves from scratch.

The code below is the logic we use to log a user in if their password is correct.
```
@app.route('/', methods=['GET', 'POST'])
def index():
  if flask.request.method == 'GET':
    return '''
    <p>Your credentials:
    username: TheCodeLearner
    password: !aehashf0qr324*&#W)*E!
    </p>
               <form action='/' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''
  email = "TheCodeLearner"
  if flask.request.form['password'] == "!aehashf0qr324*&#W)*E!":
    user = User(email="TheCodeLearner@gmail.com", username="TheCodeLearner",password="!aehashf0qr324*&#W)*E!")
    login_user(user)
    return render_template("logged_in.html", current_user=user )
  return login_manager.unauthorized()
```

## [Show Logged in user](https://www.codecademy.com/courses/learn-flask/lessons/flask-authentication/exercises/show-logged-in-user)

In the previous lesson we were able to write the login code. 
Now in this section we will show the logged in user.

Lets zoom into this code: Notice how we pass in user into the `current_user` object. 
We will be using that `current_user` object in our html.
```
def index():
 ...
 if flask.request.form['password'] == "!aehashf0qr324*&#W)*E!":
   user = User(
     email = "TheCodeLearner@gmail.com", 
     username = "TheCodeLearner",
     password = "!aehashf0qr324*&#W)*E!"
   )
   login_user(user)
   return render_template(
     "logged_in.html", 
     current_user = user     # pass the user to the logged_in.html template
   )
 return 'Bad login'
```
Now when we login successfully we are sent to a page showing our logged in info. 
Most likely in our application you will be serving dynamic pages of html. 
We can use Jinja templates to render our data from the backend. 
To display the user we pass it in from the endpoint and access that variable in our html.
```
<h1>Welcome to Our Home Page</h1>
 
<p>Welcome back {{current_user.username}}</p>
 
<a class="blue pull-left" href="{{ url_for('index') }}">back</a>
```
This will enable us to see our data when we log in!




















# Build Your First Flask App

# [Introduction](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/introduction-to-flask/lessons/flask-build-your-first-app/exercises/introduction)

[Flask](https://flask.palletsprojects.com/en/1.1.x/) 
is a popular Python framework for developing web applications. 
Classified as a microframework, it comes with minimal built-in components and requirements, making it easy to get started and flexible to use. 
At the same time, Flask is by no means limited in its ability to produce a fully featured app. 
Rather, it is designed to be easily extensible, and the developer has the liberty to choose which tools and libraries they want to utilize. 
As such, Flask is capable of creating both simple static websites as well as more complex apps that involve database integration, accounts and authentication, and more!

In this lesson, we’ll start by looking at an example of a minimal Flask application. 
It will display the text, Hello, World! on the webpage. 
You’ll learn how to create this and build on top of it in the following exercises.

## [Instantiate Flask Class](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/introduction-to-flask/lessons/flask-build-your-first-app/exercises/instantiate-flask-class)

We’ll now break down each step in creating a minimal Flask app. 
The Python module that contains all the classes and functions needed for building a Flask app is called **`flask`**.

We can begin building our app by importing the Flask class, which is needed to create the main application object, from the `flask` module:
```
from flask import Flask
```
Now, we can create an instance of the `Flask` class. 
Let’s save the application object in a variable called `app`:
```
app = Flask(__name__)
```
When creating a Flask object, we need to pass in the name of the application. 
In this case, because we are working with a single module, we can use the special Python variable, `__name__`.

The value of `__name__` depends on how the Python script is executed. 
If we run a Python script directly, such as with `python app.py` in the terminal, then `__name__` is equal to the string '__main__'. 
On the other hand, if the script is being imported as a module into another Python script, then `__name__` would be equal to its filename.

As we’ll see in the next exercise, this distinction can be useful when we have code that we want to be run only if the script is executed a particular way.

## [Routing](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/introduction-to-flask/lessons/flask-build-your-first-app/exercises/routing)

Each time we visit a URL in a browser, it makes a request to the web server, which processes the request and returns a response back to the browser. 
In our Flask app, we can create endpoints to handle the various requests. 
Requests from different URLs can be directed to different endpoints in a process called routing.

To build a route, we need to first define a function, known as a view function, that contains the code for processing the request and generating a response. 
The response could be something as simple as a string of text. 
Then, we can use the `route()` decorator to bind a URL to the view function such that the function will be triggered when the URL is visited:
```
@app.route('/')
def home():
    return 'Hello, World!'
```
The `route()` decorator takes the URL path as parameter, or the part of the URL that follows the domain name. 
All URL paths must start with a leading slash. 
In the above example, if we visit [http://localhost:5000/](http://localhost:5000) in the browser, `Hello, World!` will be displayed on the webpage.

Multiple URLs can also be bound to the same view function:
```
@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'
```
Now, both [http://localhost:5000/](http://localhost:5000) and [http://localhost:5000/home](http://localhost:5000/home) will display `Hello, World!`.

## [Render HTML](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/introduction-to-flask/lessons/flask-build-your-first-app/exercises/render-html)

The response we return from a view function is not limited to plain text or data. 
It can also return HTML to be rendered on a webpage:
```
@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'
```
We can use triple quotes to contain multi-line code:
```
@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>Hello, World!</h1>
    <p>My first paragraph.</p>
    <a href="https://www.codecademy.com">CODECADEMY</a>
    '''
```

## [Variable Rules](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/introduction-to-flask/lessons/flask-build-your-first-app/exercises/variable-rules)

We’ve seen how the `route()` decorator can be used to bind one or more static URLs to a view function. 
But what if we want to handle a set of URLs that may be constantly changing? 
Let’s take a look at how we can use variable rules to allow for dynamic URLs.

When specifying the URL to bind to a view function, we have the option of making any section of the path between the slashes (`/`) variable by indicating `<variable_name>`. 
These variable parts will then be passed to the view function as arguments. 
For example:
```
@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'
```
Now, URLs like `'/orders/john/1'` and `'/orders/jane/8'` can all be handled by the `orders()` function.

Note that we can also optionally enforce the type of the variable being accepted using the syntax: `<converter:variable_name>`. 

The possible converter types are:

types | accepts
--- | --- |
string | accepts any text without a slash (default)
int |	accepts positive integers
float |	accepts positive floating point values
path | like string but also accepts slashes
uuid | accepts UUID strings










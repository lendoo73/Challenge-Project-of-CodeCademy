# [Flask Forms](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/introduction)

## [Introduction](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/introduction)

An important role of websites is gathering information from the user. 
Whether a user is signing into their Codecademy account, ordering clothes online or leaving feedback for a company, web forms have provided a simple way to enter and submit data over the internet.

The use of forms in a site can be an involved process. 
The designer must gather the right information, display the fields in a pleasing manner and ensure the data is collected correctly. 
Over the years this has become easier thanks to frameworks like Flask, which help streamline the process of displaying fields and gathering data.

This lesson assumes a foundational knowledge of web forms and the steps involved in sending the data to the web server. 
In the following exercises we are going to look at how Flask can help gather data from regular web forms as well as create forms in an entirely new way.

## [Flask Request Object](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/flask-request-object)

Every time a client communicates with a server it does so through a *request*. 
By default our Flask routes only support GET requests. 
These are requests for data such as what to display in a browser window. 
When submitting a form through a website, the form data is sent as a POST request. 
This type of request wants to add data to the app. 
Routes can handle POST requests if it is specified in the `methods` argument of the `route()` decorator:
```
@app.route(
  "/", 
  methods = ["GET", "POST"]
)
```
The code above shows a route that now supports both GET and POST requests. 
By default `methods` is set to [“GET”]. 
When adding “POST” to a route’s methods, be sure to include “GET” if you plan for the route to handle those requests as well.

Flask provides access to the data in the request through the `request` object. 
Importing the `request` object allows us to access everything about the requests to our app including form data and the request method such as `GET` or `POST`.
```
from flask import request
```
When data is sent via a form submission it can be accessed using the `form` attribute of the `request` object. 
The `form` attribute is a dictionary with the form’s field names as the keys and the associated data as the values. 
For example, if a text input had the name "my_text", then the data access would look like this:
```
text_in_field = request.form["my_text"]
```

## [Route Selection](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/route-selection)

As sites get larger and their file structure becomes more complex the paths of Flask routes may change. 
In this case paths that are hard coded into the navigation elements such as hyperlinks and forms may break.

Flask addresses the challenge of expanding file structures with `url_for()`. 
The function `url_for()` takes a route’s function name as an argument and returns the associated URL path. 
Given the following Flask route declaration:
```
@app.route('/')
def index:
```
These two hyperlinks below are identical:
```
<a href="/">Index Link</a>
 
<a href="{{ url_for('index') }}">Index Link</a>
```
* `url_for()` is inside an expression delimiter {{ }}
* the argument for `url_for()` is inside single quotes
* the entire statement is inside double quotes

**To pass variables** from the template to the app, keyword arguments can be added to `url_for()`. 
They will be sent as arguments attached to the URL. 
It can be accessed the same way as if it was added onto the path manually:
```
<a href="{{ url_for(
  'my_page', 
  id = 1
) }}">One</a>
```
This line creates a link that sends the value `1` to the route with the function name `my_page`. 
The route can access the variable through `my_id`.
```
@app.route("/my_path/<int:my_id>"), methods = ["GET", "POST"])
def my_page(my_id):
    # Access flask_name in this function
    new_variable = my_id
    ...
```

## [FlaskForm Class](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/flaskform-class)

Flask provides an alternative to web forms by creating a form class in the application, implementing the fields in the template and handling the data back in the application.

A Flask form class inherits from the class `FlaskForm` and includes attributes for every field:
```
class CommentForm(FlaskForm):
  comment = StringField("Comment")
  submit = SubmitField("Add Comment")
```
This simple class will enable the creation of a form with a text field and a submit button.

The class inherits from the class `FlaskForm` which allows it to implement the form as template variables and then collect the data once submitted. 
`FlaskForm` is a part of [FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/).

Access to the fields of this form class is done through the attributes, `my_textfield` and `my_submit`. 
The `StringField` and `SubmitField` classes are the same as `<input type=text...` and `<input type=submit...` respectively and are part of the [WTForms library](https://wtforms.readthedocs.io/en/2.3.x/).

Below is a simple Flask app with the form class.
```
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
 
app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"         # This line is a way to protect against CSRF or Cross-Site Request Forgery.
                                               # CSRF is an attack that used to gain control of a web application.
class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")
 
@app.route("/")
def my_route():
    flask_form = MyForm()
    return render_template(
        "my_template", 
        template_form = flask_form
    )
```
In order to use this form in our template, we must create an instance of it and pass it to the template using `render_template()`. 

## [Template Form Variables](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/template-form-variables)

Creating a form in the template is done by accessing attributes of the form passed to the template.

Let’s use the following form as we work toward implementing it in a template:
```
class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")
```
In our application route we must instantiate the form and assign that instance to a template variable:
```
# app.py
my_form = MyForm()
 
return render_template(template_form = my_form)
```
Moving to the template, creating a form we simply use the form class attributes as expressions.
```
# template.html
<form action="/" method="post">
    {{ template_form.hidden_tag() }}
    {{ template_form.my_textfield.label }}
    {{ template_form.my_textfield() }}
    {{ template_form.my_submit() }}
</form>
```
* Inside the standard `<form>` are all the FlaskForm objects accessed through **`template_form`**.

* **`{{ template_form.hidden_tag() }}`** is the other end of the CSRF protection. 
While not visible in the form, this field handles the necessary tasks to protect from CSRF.
* The next two lines are for the text box. 
  * The first accesses the `label` of the field, which we specified as an argument when we created the field. 
  * The second `my_textfield` line is the input field itself.
* The last line of the form is the submit button. 
Just like the HTML version, this will initiate sending the form data back to the server.

The HTML created from this form implementation is as follows:
```
<form action="/" method="post">
    <input id="csrf_token" name="csrf_token" type="hidden" value="ImI1YzIxZjUwZWMxNDg0ZDFiODAyZTY5M2U5MGU3MTg2OThkMTJkZjQi.XupI5Q.9HOwqyn3g2pveEHtJMijTu955NU">
    <label for="my_textfield">TextLabel</label>
    <input id="my_textfield" name="my_textfield" type="text" value="">
    <input id="my_submit" name="my_submit" type="submit" value="SubmitName">
</form>
```








































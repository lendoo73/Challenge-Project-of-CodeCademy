# [Flask_Templates](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/introduction)

## [Introduction](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/introduction)

When you navigate through a website you may notice that many of the pages on the site have a similar look and feel.
This aspect of a website can be achieved with the use of *templates*.
In this lesson the term template refers to an HTML file that can represent multiple web pages with the same structure and functionality.

Flask uses the [Jinja2 template engine](https://jinja.palletsprojects.com/en/2.11.x/) to render HTML files that include application variables and control structures. 
The Jinja2 template engine is a powerful tool that supports an organized and growth oriented application.

In this lesson we will look at:
* How to organize our site file structure
* Use our application data with our templates
* Leverage control structures within our templates
* Share common elements across many templates

## [Rendering Templates](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/rendering-templates)

Containing our HTML in files is the standard and more organized approach to structuring our web app.

To work with files, which we will call templates, we use the Flask function `render_template()`.
Used in the return statement, this function takes a template file name as an argument and returns the content to send to the client.
It uses the Jinja2 template engine to generate HTML using the template file as blueprint.
To use `render_template()` in our routes we need to import it from the `flask`.
```
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")
```
Inside the application directory `render_template()` looks for templates inside a directory called **templates**.
All template files should be kept inside this directory. 




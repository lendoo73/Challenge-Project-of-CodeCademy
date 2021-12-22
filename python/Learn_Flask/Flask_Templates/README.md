# [Flask Templates](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/introduction)

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
```py
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")
```
Inside the application directory `render_template()` looks for templates inside a directory called **templates**.
All template files should be kept inside this directory. 

## [Template Variables](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/template-variables)

After the filename argument in `render_template()` we can add keyword arguments to be used as variables within the template. 
These variables are assigned values or app data we would like to access within the template.
```py
flask_variable = "Text for my template"
 
render_template(
  "my_template.html", 
  template_variable = flask_variable
)
```
We’re assigning the value of `flask_variable` to `template_variable` which can be used in **my_template.html**.
To add more than one variable separate each assignment with a comma.
```py
render_template(
  "my_template.html", 
  template_var1 = "A string!", 
  template_var2 = 100
)
```
Our template now has access to the variables template_var1 and template_var2 which hold a string and an integer.
App data can be passed as literal values or the values stored inside variables. 
We can pass strings, integers, lists, dictionaries or any other objects to our templates.

To access the variables in our templates we need to use the expression delimiter: `{{ }}`.

The delimiter can be used inline with text and alongside HTML elements.
```py
<h1>My Heading: {{ template_variable }}</h1>
```
Certain operations can be performed inside expression delimiters {{ }}.
```py
<p>Template number plus ten: {{ template_variable + 10 }}</p>
```
List and dictionary elements can be accessed individually inside the expression delimiters {{ }}.
```py
<p>Element at index 1: {{ template_list[1] }}</p>
```

## [Variable Filters](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/variable-filters)

*Filters* are used by the template engine to act on template variables. 
To use them simply follow the variable with the filter name inside the delimiter and separate them with the `|` character.
```py
{{ variable | filter_name }}
```
The filter title acts on a string variable and capitalizes the first letter in every word. 
Given the variable assignment `template_heading = "my very interesting website"`.
```py
{{ template_heading |  title }}
 
OUTPUT
My Very Interesting Website
```
Filters can also take arguments. 
The `default` filter will output the text in its argument when a variable isn’t passed to the template. 
Consider if `no_template_variable` is missing from the `render_template()` arguments.
```py
{{ no_template_variable | default("I am not from a variable.") }}
 
OUTPUT
I am not from a variable.
```
The default filter does not work on empty strings "" or None values.

While filters perform more complex functions than simple operators, they are still small, focused actions. 
Here is a list of commonly applied filters and their descriptions. 
* `title`: Capitalizes the first letter of each word in a string, known as titlecase
* `capitalize`: Capitalizes the first character of a string, such as in a sentence
* `lower`/`uppercase`: Makes all the characters in a string lowercase/uppercase
* `int`/`float`: Changes any number variable to an integer/float
* `default`: Defines a default string if the variable is not defined
* `length`: Calculates the length of a string, list or dictionary variable
* `dictsort`: Sorts a dictionary by its keys

More information can be found in the [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters)

## [If Statements](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/if-statements)

Including conditionals such as if and if/else statements in our templates allows us to control how data is handled.

Let’s say we have a string variable passed to our template. When the variable contains an empty string will you want to output it or will you want to output another string? Remember the `default` filter doesn’t work in this situation so an if statement is needed.

Using if statements in a template happens inside a statement delimiter block: {% %}.
```py
{% if condition %}
  <p>This text will output if condition is True</p> 
{% endif %}
```
Notice the `{% endif %}` delimiter is necessary to close the if statement.

The condition can include a variable that is tested using standard comparison operators, `<`, `>`, `<=`, `>=`, `==`, `!=`.
```py
{% if template_variable == "Hello" %}
  <p>{{template_variable}}, World!</p> 
{% endif %}
```
While inside statement delimiters `{% %}` we can access variables without using the usual expression delimiter `{{ }}`.

Variables can also be tested on their own. 
A variable defined as `None` or `False` or equates to `0` or contains an empty sequence such as `""` or `[]` will test as **False**.

The `{% else %}` and `{% elif %}` delimiters can be included to create multi-branch if statements.
```py
{% if template_number < 20 %}
  <p>{{ template_number }} is less than 20.</p> 
{% elif template_number > 20 %}
   <p>{{ template_number }} is greater than 20.</p> 
{% else %}
   <p>{{ template_number }} is equal to 20.</p> 
{% endif %}
```

## [For Loops](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/for-loops)

Repetitive tasks are standard in most computer applications and template rendering is no different. 
Creating lists, tables or a group of images are all repetitive tasks that can be solved using for loops.

Using the same statement delimiter block as if statements `{% %}`, for loops step through a range of numbers, lists and dictionaries.
The following code will create an ordered list where each line will output the index of the sequence:

```py
<ol>
{% for x in range(3) %}
  <li>{{ x }}</li>
{% endfor%}
</ol>
```
The local loop variable can be used inside our loop with the expression delimiter `{{x}}`.
Similar to the if statements we need to close the loop with an `% endfor %} block`.

### Iterate through a list variable:

```py
{% for element in template_list %}
```

### Iterate through a string:

```py
{% for char_in_string in “Hello!” %}
```

### Iterate through the keys of a dictionary variable:

```py
{% for key in template_dict %}
```

### Iterate through keys AND values of a dictionary with `items()`:

```py
{% for key, value in template_dict.items() %}
```
Using the filter `dictsort` in a loop outputs the key/value pairs just like `items()`.

## Inheritance

If you go to any website you may notice certain elements exist across different web pages.

The navigation bar is a good example of a common page element. 
This is the banner at the top of most sites that has links to different pages. 
No matter what page you’re on the navigation bar is there.

Imagine having separate files for each web page and wanting to make a change to the navigation bar. 
Would you have to change the content of every template of the site? 
No, that would take too long.

To solve this problem template files are used to share content across multiple templates. 
The simplest case is a file that includes the top portion of the templates through the `<body>` tag and then the closing `</body>` and `</html>` tags. 
Jinja2 statement delimiters are then used to identify the area of the template where specific content will be substituted in.
```py
# base.html
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
  {% block content %}{% endblock %}
  </body>
</html>
```
To inherit this content in another template we will use the `extends` statement. 
The code to be substituted should then be surrounded by `{% block content %}` and `{% endblock %}`. 
All together this looks like the following template:
```py
# index.html
{% extends "base.html"  %}
 
{% block content %}
    <p>This is my paragraph for this page.</p>
{% endblock %}
```
When a route returns `render_template("index.html")` the rendered page will have this content.
```py
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
    <p>This is my paragraph for this page.</p>
  </body>
</html>
```

### [Run on Glitch](https://flask-templates.glitch.me)

[Code on Glitch](https://glitch.com/edit/#!/flask-templates)

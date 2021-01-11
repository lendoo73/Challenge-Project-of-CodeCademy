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

## [Template Variables](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/template-variables)

After the filename argument in `render_template()` we can add keyword arguments to be used as variables within the template. 
These variables are assigned values or app data we would like to access within the template.
```
flask_variable = "Text for my template"
 
render_template(
  "my_template.html", 
  template_variable = flask_variable
)
```
We’re assigning the value of `flask_variable` to `template_variable` which can be used in **my_template.html**.
To add more than one variable separate each assignment with a comma.
```
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
```
<h1>My Heading: {{ template_variable }}</h1>
```
Certain operations can be performed inside expression delimiters {{ }}.
```
<p>Template number plus ten: {{ template_variable + 10 }}</p>
```
List and dictionary elements can be accessed individually inside the expression delimiters {{ }}.
```
<p>Element at index 1: {{ template_list[1] }}</p>
```

## [Variable Filters](https://www.codecademy.com/courses/learn-flask/lessons/flask-templates/exercises/variable-filters)

*Filters* are used by the template engine to act on template variables. 
To use them simply follow the variable with the filter name inside the delimiter and separate them with the `|` character.
```
{{ variable | filter_name }}
```
The filter title acts on a string variable and capitalizes the first letter in every word. 
Given the variable assignment `template_heading = "my very interesting website"`.
```
{{ template_heading |  title }}
 
OUTPUT
My Very Interesting Website
```
Filters can also take arguments. 
The `default` filter will output the text in its argument when a variable isn’t passed to the template. 
Consider if `no_template_variable` is missing from the `render_template()` arguments.
```
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
```
{% if condition %}
  <p>This text will output if condition is True</p> 
{% endif %}
```
Notice the `{% endif %}` delimiter is necessary to close the if statement.

The condition can include a variable that is tested using standard comparison operators, `<`, `>`, `<=`, `>=`, `==`, `!=`.
```
{% if template_variable == "Hello" %}
  <p>{{template_variable}}, World!</p> 
{% endif %}
```
While inside statement delimiters `{% %}` we can access variables without using the usual expression delimiter `{{ }}`.

Variables can also be tested on their own. 
A variable defined as `None` or `False` or equates to `0` or contains an empty sequence such as `""` or `[]` will test as **False**.

The `{% else %}` and `{% elif %}` delimiters can be included to create multi-branch if statements.
```
{% if template_number < 20 %}
  <p>{{ template_number }} is less than 20.</p> 
{% elif template_number > 20 %}
   <p>{{ template_number }} is greater than 20.</p> 
{% else %}
   <p>{{ template_number }} is equal to 20.</p> 
{% endif %}
```





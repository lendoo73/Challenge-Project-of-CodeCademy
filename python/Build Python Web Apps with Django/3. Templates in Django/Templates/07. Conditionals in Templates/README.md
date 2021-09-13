#### TEMPLATES

# [Conditionals in Templates](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/conditionals-in-templates)

Now that we have covered variables, we can start using `if` statements. 
These `if` statements help customize web pages without having to create separate templates for different instances. 
Imagine if we have an application that shows information for different US cities. 
Making individual templates for each city could take ages! 
Instead, we can use `if` statements to determine what city’s information to display.

An `if` statement in DTL is very similar to Python `if` statements. 
However, they consist of **two necessary components** and **two optional components**. 
**The major components** are:
* An `if` keyword is used in every `if` statement and its purpose is the same as in Python.
* An `endif` keyword is used to let DTL know that we are at the end of the `if` statement.

**The two optional components** are:
* `elif` - which is used if we want to check more than one condition within the `if` statement.
* `else` - which will execute whenever the `if` and all `elif`s evaluates as false. 
It will be the last thing included in an `if` statement before the `endif`.

To add an `if` statement to the template, we’ll need to set it up inside of tags. 
Remember, tags are the `{%` and `%}` symbols we used earlier for extending our base template to other templates. 
Generally, tags are used to tell the DTL that an expression needs to be executed or evaluated. 
There is no need to use separate variable tags when accessing a variable in normal tags. 
For instance, if we wanted to display attractions for New York or Los Angeles, we could use the following conditional:
```html
{% if city.name == "New York" %}
  <p>Attractions for New York City are</p>
  ...
{% elif city.name == "Los Angeles" %}
  <p>Attractions for Los Angeles are</p>
  ...
{% else %}
  <p>We currently do not have any attractions for that city</p>
{% endif %}
```
Notice that we can use the same `{% %}` tags to create these conditionals within the template, and help tell the DTL what to render. 
This makes sure that only certain elements get rendered based off the conditionals detailed.

Other conditionals can be used other than just `==`. 
Any conditional that is conventionally used with Python conditional statements. 
Lessons are available if you want [refresher on conditionals](https://www.codecademy.com/courses/learn-python-3/lessons/python-control-flow/exercises/introduction).

#### TEMPLATES

# [Variables in Templates](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/variables-in-templates)

Let’s explore this *Django Template Language*, or *DTL*, we’ve been using in the previous exercises. 
DTL, as its name implies, is a template language created specifically for Django. 
Its primary purpose is to help reduce the amount of code necessary for running a webpage. 
We’ve seen how DTL can extend templates and load in CSS files. 
But, DTL can do so much more for us, like 
* grabbing variables from **views.py**, 
* creating loops, 
* if statements, 
* and more! 

In this exercise, we’ll start with creating variables.

We’ll cover the specifics of how views provide variables for templates in a later lesson. For now, we’ll just review the syntax for evaluating variables — two symbols are needed, {{ and }}, we call these symbols variable tags. When we add a variable in between variable tags, Django knows that we want the value of that variable from our views.py file.

For example, if we had an application that wanted to output a specific username, we would add our variable tags with the variable name inside of these tags, that being username:

<p>{{ username }}</p>
Dictionaries and variable tags work well together. In a single variable tag, we can grab a dictionary and access all its properties! Imagine if we stored our user’s information in a dictionary named user:

<p>{{ users.username }}</p>
Notice we’re able to use dot notation to access the .username property of user. In an actual app, there should be more properties we can access. We’ll cover how to access each individual property later when we discuss DTL loops but now it’s time to practice using variable tags.

#### TEMPLATES

# [Adding CSS to the Templates](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/adding-css-to-the-templates)

In most applications, HTML files will usually use a CSS file to modify how the webpage looks. 
While we won’t be covering CSS specifically in this exercise, 
we will be covering how to add CSS files to our templates as the process is different in Django templates compared to a normal HTML document. 
To learn more about CSS, we recommend our [Learn CSS course](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/adding-css-to-the-templates).

We need a folder to store our CSS files, this folder will be in the application’s main folder and called **static/**. 
This folder will hold assets like pictures and CSS files. 
Another folder will be created inside of **static/** that will be named after our application. 
The full path should look like the one below:
```txt
projectname/
 |-- appname/
     |-- templates/
     |-- static/
         |-- appname/
             |-- file.css
```
Once a CSS file is added to static/appname, it can be referenced within our templates inside of blocks formed in the base.html <head> elements. This is because static files will not be passed down to children of the base.html template. The files in our static/ folder should be loaded in the <header>. Therefore, we’ll add another block tag, like so:

<!-- base.html -->
<!DOCTYPE html>
<head>
  {% block head %}
 
  {% endblock %}
</head>
...
Inside of the template we’ll be using, we first need to load in static files. This is typically done at the beginning of the file after extending from base.html. This will let us access all of our static files later. Then the block created from base.html can be added to the document. This is the block where the CSS will be loaded in. This is done by loading a CSS file as normal, except setting the href to a tag that says {% static 'appname/file.css' %}. It should look like the code below.

<!-- template_example.html -->
{% load static %}
 
{% block head %}
<link rel="stylesheet" href="{% static 'appname/file.css' %}">
{% endblock %}

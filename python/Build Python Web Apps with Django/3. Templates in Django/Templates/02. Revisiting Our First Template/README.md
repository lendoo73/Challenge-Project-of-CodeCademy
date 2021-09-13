#### TEMPLATES

# [Revisiting Our First Template](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/revisiting-our-first-template)

The first template usually made is the homepage of the application. 
Templates can be plain HTML files and are stored inside of **appname/templates/appname/**. 
While the template can usually be left as a normal HTML file, 
most of the time *Django Template Language* or *DTL* will be added to the template to assist with the creation of the application. 
If you want to go into more detail regarding how to build the application using plain HTML, check out our [course here](https://www.codecademy.com/learn/learn-html). 
Please note that this lesson will be using DTL and HTML throughout the exercises. 

When any template is referenced later, it will be done by calling `appname/template_name.html`. 
This is to help the Django engine find the template because DTL will not look in any sub folders in the template folder for files.

Once the template is made, some of the code in **views.py** will have to be modified in order to render the template. 
Rendering the template is the Django application taking the template and displaying it as a normal HTML page in a web browser.

Inside of **views.py**, we need functions, or classes, that tell the template what information to include. 
For example, one function (`homepage()`) will be created that takes in one parameter called `request`. 
The `homepage()` function will return another function called `render()` that takes two arguments.
The first being the request that gets passed into `homepage()`, and the name of the template. 
Just as a refresher, the final method in **views.py** should look like the one below:
```py
def homepage(request):
  return render(request, "app_name/sample_template.html")
```
These modifications to **views.py** will be covered in more detail in a later lesson. 
In this lesson, the code for **views.py** will be provided so that we can focus primarily on templates and not the views.

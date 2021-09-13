#### TEMPLATES

# [Review](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/review)

Templates are a great way to reduce the amount of HTML that needs to be written in a website by 
allowing us to extend templates into the rest of the website to reduce repeat code. 
The options provided to us can help us in a number of ways including:
* Common elements should go inside of a base template, and any page-specific content should be in their own templates.
* Static files have to be loaded in the template they’ll be used in, as it won’t be passed on to child templates.
* Templates can also use DTL to help display variables, loop through and display dictionaries, 
and create conditionals within templates to reduce the number of templates needed for an application.
* CSS files can be added to a template after adding a **static/** folder to the application. 
Remember that inside of **static/** there should be another folder named after the application.
* Variables are great for grabbing data from **views.py** to display in a template.
* `if` statements can be used in DTL to conditionally display content.
* DTL can use `for` loops to go through lists.
* URLs can be referenced with just the path name if the page is within the application. 
This only works with predefined paths and you should watch for any arguments that need to be passed.
* Filters are useful for modifying variables within a template as you won’t have to write too much extra code to modify the variable yourself.
* Some filters require arguments, so make sure that any filter used does not require any arguments.
* Some filters also only work with specific data types, so make sure to research a filter before using one by looking at the documentation for the filter.

Great job on completing templates! Next time you write HTML in Django, remember to take advantage of DTL to save yourself some time!

#### 

# [Filters in Templates](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/filters-in-templates)

With Django, variables can be modified from within the template using a *filter*. 
Filters modify variables passed in from **views.py** without the use of traditional methods like JavaScript. 
There are plenty of filters that can be found in the [Django documentation](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/)
, but we’ll only cover a few in this lesson. 
An example filter can be seen below:
```html
<p>{{ username|upper }}</p>
```
The filter is added onto a variable by using the `|` symbol inside of the variable tags with the variable. 
The symbol goes after the variable name, and is followed by the filter that you want to use. 
In the above example, the [upper filter](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#upper)
converts the variable’s value to all uppercase characters.

Some filters also require arguments, however, arguments are handled differently with filters compared to how we handled arguments with URL. 
A filter with an argument can be seen here:
```html
{{ description|truncatewords_html:2 }}
```
The `truncatewords_html` filter requires an argument and will shorten text down to the integer supplied by our argument. 
In our case, we want to display `2` words max. 
Any other words in the description variable will be replaced with `...`. 
We were able to supply our argument after the filter name separated by a `:`.

Some filters also require certain data types in order to work. 
For instance, the `time` filter requires a variable of data type `datetime.datetime.Now()`, and will not work with any other data type. 
It is recommended to check out the documentation for a filter before using it to make sure you are using the proper data types and adding any necessary arguments.

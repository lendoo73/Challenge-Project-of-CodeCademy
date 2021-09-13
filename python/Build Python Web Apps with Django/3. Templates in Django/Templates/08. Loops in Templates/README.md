#### TEMPLATES

# [Loops in Templates](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/loops-in-templates)

When dealing with a dictionary in a Django template, we can save time by taking advantage of DTL’s `for` loop to iterate over individual items. 
Loops in DTL work like regular Python `for` loops but still require tags.

To write a loop in DTL we’ll need to use our tags `{% %}` and insert the syntax for a `for` loop. 
The syntax to start a `for` loop requires:
* The `for` keyword.
* The name of the new variables we’ll be creating in the loop.
* An indicator saying `in`
* The list we’ll be using in the loop.

Those will all be listed out in that order, and will be followed with an `{% endfor %}` at the end of the loop. 
The loop syntax looks like:
``` html
{% for item in list_name %}
  <p>{{ item }}</p>
{% endfor %}
```
Inside the loop’s body, during each iteration, we can access the current key using the temporary variable `key` inside variable tags `{{` `}}`. 
We’re free to manipulate the key as a variable using standard Python syntax. 
If our list contains dictionaries, we could even access the `value` of our dictionary if we change our loop:
```html
{% for key, value in dictionary_list %}
  <p>{{ key }} : {{ value }}</p>
{% endfor %}
```
Using loops, we can greatly reduce the amount of HTML we need to write to display a lot of information!

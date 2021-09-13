#### TEMPLATES

# [Adding URLs to a Template](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/adding-urls-to-a-template)

When navigating between pages using HTML, we need the entire URL to be written out in a [`<a>` element’s](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
`href` attribute. 
With Django, rather than using the full URL we get a shortcut by using tags and the name of predefined paths! 
Later on, we’ll also cover how to pass along data in the URL, however, let’s first see the basic shortcut in action:
```html
<a href="{% url 'path_name' %}">Sample link</a>
```
As can be seen above, the link looks very similar to a typical HTML link, except we modify the `href` to be set to a tag much like we did with CSS files. 
This tag is set to the type `url` followed by the path name as a string.

When a path requires arguments to get to, like a username, it can be added to the `href` after the path. 
We won’t go into detail regarding this, but it would look like this:
```html
<a href="{% url 'path_name' username %}">User Profile</a>
```
In this case, arguments provide additional information to the URL to access more specific pages. 
Some DTL functions require arguments while they can be optional in other places. 
The URL is a good instance of where arguments are optional, but not necessary unless the path has an argument. 
We’ll discuss arguments more in the next exercise.

#### TEMPLATES

# [Extending the Base Template](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/extending-the-base-template)

With our base template created, we can *refactor* our other templates by removing the common elements. 
Let’s say we wanted to refactor a template for an `about/` page, it might look like:
```py
<p>Welcome to your local veterinarian's office!</p>
 
<p>Feel free to call us at 123-456-7890!</p>
```
To use our base template in other templates, we need to include {% extends "appname/base.html" %} at the top of our about/ page template:

{% extends "vetoffice/base.html" %}
 
<p> We're all about caring for pets!</p>
<p> Contact us at: 123-456-7890 </p>
But this code isn’t complete, we still need to tell our base.html what block of content to include. This can be done by adding two tags to our document before and after the paragraphs that says block content and endblock.

{% extends "vetoffice/base.html" %}
 
{% block content %}
<p>This will go inside the body</p>
 
<p>This will also be inside the body</p>
{% endblock %}
Notice that all we had to do was add three lines of DTL, and all of our HTML from our base template is now added to the template.

Now that that both templates are set up, all of our common code can go inside of base.html, and any page-specific content can go inside of template.html. This will help with not only keeping the code organized, but also help make the code cleaner as we’ll only be seeing page-specific content in the templates from now on.

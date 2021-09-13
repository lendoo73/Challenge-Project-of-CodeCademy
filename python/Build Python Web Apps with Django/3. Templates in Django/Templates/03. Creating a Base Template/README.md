#### TEMPLATES

# [Creating a Base Template](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/templates-in-django/modules/django-templates/lessons/django-templates-lesson/exercises/creating-a-base-template)

We’ve now created a simple home page, but we’re missing some elements like a helpful navigation bar to move around the application. 
A basic navigation bar looks like the following. 
(Please note that we’ll be ignoring CSS for now)
```html
<div class="topnav" id="pageTopNav">
  <a href="#home" class="active">Home</a>
  <a href="#contact">Contact</a>
</div>
```
Now imagine if we included even more links, this navigation bar could grow really large! 
This means each page that contains this code would continue to grow along with it. 
Django solves this issue of copying and pasting the same reused code from each template into something one template called a *base template*. 
Some elements that might go into the base template are: 
* headings, 
* navigation bars, 
* footers, etc 
these elements show up on most, if not all of the web pages for the application.

A base template is created the same way as a normal template, starting with an HTML file. 
By convention, the base template is usually called something like **base.html** or **base_template.html**. 
For this lesson, we’ll be using **base.html** as the name.

Once the common elements have been moved to **base.html**, we can start talking about adding page-specific content. 
Since the **base.html** will be used across several templates, we need to tell the application where we want our page-specific content to go. 
To do this, we add tags to the body of the base template. 
Tags are used to help extend the base template to other templates. 
We’ll be going over this in more detail in another exercise, but for now, we just need to know that tags are created using the `{%` and `%}` symbols. 
Inside of these tags, we’ll be adding `block content`, and later another tag with the content `endblock`. 
This creates a block that we can add code to in other templates. 
This block gives us the ability to later insert content that is specific to individual pages. 
It should look like this:
```html
{% block content %}
 
{% endblock %}
```
Typically only page-specific content will go inside of these tags and is added from other templates. These blocks are usually left empty in the base template though. Multiple blocks can be created within the base template and then used in other templates. Blocks can be put anywhere within the base template. This is because not everything page-specific will necessarily go in the body.

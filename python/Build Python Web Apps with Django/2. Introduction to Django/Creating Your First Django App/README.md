#### CREATING YOUR FIRST DJANGO APP

# [Introduction to Django](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/introduction-to-django)

Welcome to the world of Django!

Django, pronounced like JANG-go with a silent D, is a high-level web framework that is written with Python — one of the most readable and beginner-friendly programming languages. 
Django can be used to rapidly build complex database-driven websites. 
Like Python, Django is often considered to be strongly opinionated. 
An opinionated software has guidelines and defaults, such as code structure, project structure, for developing code. 
Django’s opinionated approach means specific ways of writing code and a steeper learning curve to apply the 
[“Django philosophy“](https://docs.djangoproject.com/en/3.1/misc/design-philosophies/). 
However, it comes with advantages when onboarding new teammates to a project and debugging code because of how structured a Django project is.

Django is an open-source project, supported by the 
[Django Software Foundation](https://www.djangoproject.com/foundation/)
, and has a strong community of contributors. 
It has been used by many well-known data-heavy websites such as Instagram, Youtube, and Dropbox. 
In this lesson, we’ll create together our first Django app! 
More importantly, we’ll experience first-hand how its design helps to take applications from concept to completion using its “batteries included” approach.

# [What is a Web Framework?](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/what-is-a-web-framework)

Let’s first establish what it means when we say ***Django is a web framework***.

Web frameworks are a type of software development tool that makes it easier and faster to develop web applications. 
They are a type of code library that provides code and patterns for database access, as well as templating systems for content. 
They promote code reuse, so we don’t have to write as much code to get a project running. 
Some features most web frameworks include are:
* URL routing
* Input form management and validation
* Templating engines for HTML and CSS
* Database configuration
* Web security
* Session repository and retrieval

Out of the box, Django comes with an admin panel, a user authentication system, a database, 
and something called object-relational mapper (ORM) that helps a web application interact with a database. 
These are some of the “batteries” included in Django to help build projects faster without having to worry about which tools to use.

Later we’ll see how we can bootstrap a fully featured web application in only a handful of commands.

# [How Django Works](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/how-django-works)

Before we create our first Django web app, let’s take a little look into how Django works underneath the hood. 
The Django project describes itself as an MTV framework, using Models, Templates and Views. 
Let’s break down these components:
* The model portion deals with data and databases, it can retrieve, store, and change data in a database.
* The template determines how the data looks on a web page.
* The view describes the data to be presented, and passes this information to the template.

With the basics of the components explained let’s understand how they work together when we visit a Django website. 
When a request comes to a web server, it’s passed to Django to figure out what is requested. 
A client requests a URL, let’s use codecademy.com as an example, Django will take the web address and pass it to its urlresolver. 
Django will try to match the URL to a list of patterns, and if there is a match, then pass the request to the associated view function.

Imagine a mail carrier delivering a letter. 
They walk down the street checking each house number until they find the exact one on the letter. 
Once they find the house, they deliver the letter. 
That’s how the urlresolver works!

When we land on the right page, Django uses data from the model and feeds it into the view function to determine what data is shown. 
That data is given to the template and presented to us via the web page.

This is a bit of a simplified version of what Django is doing underneath the hood, but a key takeaway is that Django follows this MTV pattern.

# [Starting a Django Project](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/starting-a-django-project)

Now that we have a basic understanding of what Django is and how it works, let’s get started with creating a project. 
Django provides us with `django-admin`, a command-line utility that helps us with a variety of administrative tasks. 
We can use it with various commands by calling it in the terminal like this:
```py
django-admin <command> [options]
```
Running `django-admin help` will provide a list of possible commands.

A Django project can be easily created with the `startproject` command. 
It takes a couple of options– the name of the project and optionally the directory for our project. 
The full command would look like this:
```py
django-admin startproject projectname
```
Django will then create a directory for the project, or the project root folder.
```py
my-project/
  ├── my-project/
  └── manage.py
```
Inside the project root folder is a Python file, **manage.py**, that contains a collection of useful functions used to administer the project. 
This file performs the same actions as `django-admin` but is set specifically to the project. 
We can do a number of things with it, such as starting a server.

Alongside the **manage.py** is another directory with the same name as the project. 
This folder is treated as a [Python package](https://docs.python.org/3/reference/import.html#regular-packages) 
because of the presence of **__init__.py**, and inside this directory contains important settings and configuration files for the project.

We’ll start a project in this exercise, and in the next exercise we will go into more detail about the specific files that are created.

# [Configuring Django Settings](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/configuring-django-settings)

With only a one-line command, Django has started a functioning project! 
Behind the scenes, Django will do all the configurations for us and store them in an inner directory with the same name as the project. 
Important for us are **settings.py** and **urls.py**. 
We can safely ignore the other files, just remember to not delete them by accident!

**settings.py** is a Python file that contains configurations that we’ll be editing throughout the development of our project. 
Inside, there is a list called `INSTALLED_APPS` which contains the apps that make up the Django project, more on these later. 
After running the `startproject` command, our **settings.py** should contain:
```py
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]
```
We can see that Django pre-installs some common apps for us, such as admin, authentication, sessions, and an app to help manage static files. 
When we create new applications for the project, we have to include them here so that Django will know about them!

Further down in **settings.py**, is a dictionary named `DATABASES`. 
It looks like:
```py
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}
```
We see that Django by default will set up an SQLite database for us. 
In later lessons, we’ll learn how to use it to store content.

Next, in the same directory where **settings.py** is located, is another Python file named **urls.py**. 
Inside are the URL declarations for this Django project, or a “table of contents” for the Django project. 
Remember earlier when we said that Django goes down a list of patterns to match a URL? 
This is that list!

When we first create the project, **urls.py** will include this:
```py
urlpatterns = [
  path('admin/', admin.site.urls),
]
```
This means that the admin app already has a route.

Since the project comes pre-configured, we can start a server to test that the project works. 
A development server can be started by using **manage.py** and providing the `runserver` command. 
This command must be run in the root directory, the same directory where **manage.py** is located. 
By default, Django will start a development server with port 8000, but an alternate port can be provided as an option.

The full command will look like this:
```py
python3 manage.py runserver <port number>
```
The Django development server will hot-reload as changes are made to the project, so we don’t have to keep restarting the server as we develop. 
The server will keep running until we stop it with the `ctrl + c`.

**Note:** Our Codecademy Django environment must run the development server on port 4001 by providing the option `0.0.0.0:4001` This port is specific to working on Codecademy. 
If you want to work locally on your computer, you can let Django set the default port for you.

# [Migrating the Database](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/migrating-the-database)

When we started the server, Django gave us an error message that there were unapplied migrations:
```py
You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
A migration is a pending database change. 
As we saw in **settings.py**, by default, Django will have some apps installed. 
Some of these default apps, for example, the admin interface, use the database and the migrations must be applied to the SQLite database.

Whenever we make changes to the model of the database, we must apply the changes by running `python3 manage.py migrate`. 
After applying the migration, when we run the server our errors are gone.

By applying our migration, we have access to the admin app! 
The admin app comes pre-installed and can be navigated to since it has its URL provided in **urls.py** we saw earlier. 
At the moment there aren’t any admin users but we can still visit `localhost/admin` to see the admin login page.

# [Django Apps](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/django-apps)

We’ve been talking about Django projects and apps for a while, but what exactly are apps? 
How are apps different from a project? 
Well, a Django app is a submodule to a project, that contains the code for a specific feature. 
In the submodule, we’ll find things like: a **models.py** file, a migration directory, and other files and directories related to the application. 
Django apps should be self-sufficient and in theory, can be picked up and placed in another project without any modification. 
A Django project refers to the entire code base and its parts. 
The Django project folder holds **manage.py** and the other module that includes **settings.py**.

In a real-world example, think of a website for a veterinarian’s office as a Django project. 
It would consist of smaller apps, such as an appointment calendar, patient profiles, and perhaps a testimonial section. 
Apps are part of what makes Django projects so scalable. 
Since they should be entirely self-sufficient, they shouldn’t break any parts as more features are added to a project. 
A Django app can be created by running the `startapp` command in the project root directory, the directory with **manage.py**, and providing the name of the app as an additional option.
```py
python3 manage.py startapp myapp
```
This will create a new directory called **myapp** alongside the project settings folder. 
Running `startapp` will result in the following folder structure.
``` py
mysite/
├── manage.py
└── mysite/
   ├── __init__.py
   ├── settings.py
   └── urls.py
└── myapp/
```
Inside our project root folder, we have our previous folder which held our project settings and a new folder for our app. 
Inside it are files related specifically for the app such as **models.py** and **tests.py**.

In order for Django to be aware of the app’s existence, it needs to be added to the list of `INSTALLED_APPS` in the project’s **settings.py** file.
```py
INSTALLED_APPS = [
  "myapp.apps.MyappConfig"
]
```

# [Creating a View for an App](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/creating-a-view-for-an-app)

Earlier, we discussed the MTV pattern and the integral role that views play. 
They are the information brokers in a Django application that decides what data gets delivered to a template and displayed. 
More simply put, a view is a class or function that processes a request and sends a response back.

In our veterinarian’s office example website, a customer might go to the `/profile` page of the website and their request gets passed to a view function to be processed. 
The view function may:
1. Check to see if the customer is logged in
2. Request their profile information from a database
3. Format the information in a template
4. Send back the profile page as an HTML file for the customer to view in their browser

The view function does quite a bit of work!

At the core, Django uses a protocol called, [Hypertext Transfer Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP)
, which is the foundation for data communication on the worldwide web. 
In Django, requests, and responses are handled as `HttpRequest` and `HttpResponse` objects from a module called `django.http`.

When a page is requested:
1. Django creates an `HttpRequest` object that contains information about the request
2. Django loads the appropriate view, passing the `HttpRequest` as the first argument to the view function

Each view function is responsible for returning an `HttpResponse` object. 
The `HttpResponse` response object can be 
* the HTML contents of a web page, 
* a redirect, 
* an error, 
* an XML document, 
* an image, 
* or just about anything that can display on a web page.

A simple view function would look like this:
```py
# In views.py
def index(request):
  return HttpResponse("This is the response!")
```
Above, we have an `index()` view function for our home page. 
When users visit our home page, the view function sends back an `HttpResponse` with the string `"This is the response!"` to be displayed on a web page.

# [Using a View To Send an HTML Page](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/using-a-view-to-send-an-html-page)

We just made a view that sends raw text to the browser. 
But, websites aren’t just plain text! 
In order to create stylish web pages, we mainly use HTML, CSS, and JavaScript.

We can use Django to render an HTML page when a view function is called. 
Django will look in each app folder inside `INSTALLED_APPS` for directories named **templates**. 
The [best practice](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#namespacing-url-names) 
for structuring this folder is to *namespace* them. 
That is to place our HTML pages inside a directory that has the same name as your app within the **templates/** directory.

The resulting templates folder structure will look like this:
```py
myapp/
└── templates/
    └── myapp/
      └── mytemplate.html
```
The reason for this nested structure is if there was a template file with the same name in a different application, Django would be unable to distinguish between them. 
We need to be able to point Django at the right one and namespacing them ensures against future conflicts, 
so that apps lower down in the `INSTALLED_APPS` setting do not override previous templates.

With our file structure set up, we can build out the logic in our view function in **views.py** like so:
```py
from django.template import loader
def home():
  template = loader.get_template("app/home.html")
  return HttpResponse(template.render())
```
In the above code, we import `loader` from `django.template`. 
Inside the view function (`home()`) we load the template with `.get_template()`. 
Then, we use the `.render()` method on the template object inside the `HttpResponse` object to send HTML pages to clients.

# [Creating a Django Template](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/introduction-to-django/modules/introduction-to-django/lessons/creating-your-first-django-app/exercises/creating-a-django-template)

To place content generated from Django inside the HTML file, we need to turn our static HTML file into a *template*.

In the context of a web framework, templates are pages created with special markup that allows for backend data and commands to modify the contents of a page. 
Django employs a special syntax called *Django Templating Language* to distinguish itself from HTML, CSS, and JavaScript. 
That syntax in many template languages uses curly braces, sometimes referred to as *handlebars*, as a placeholder for data that is passed by Django.

In the HTML, we use curly braces the braces like this:
```HTML
<h1>Hello, {{name}}</h1>
```
When we call the view to render the template, we can use something called a context to tell Django what to replace in the template. The relationships in the context are referred to as a name/value pair. By default, a context is an empty dictionary. Our context for name will look like this inside the view function:

context = {"name": "Junior"}
We then pass the context as an argument in the render function. The full view.py will look like this:

from django.http import HttpResponse
from django.template import loader
def home(request):
  context = {"name": "Junior"}
  template = loader.get_template("app/home.html")
  return HttpResponse(template.render(context))
This would return a webpage that says “Hello, Junior” inside an <h1> tag.

It’s quite common in Django to load templates, fill their context, and return an HttpResponse object with their rendered template. Django provides a shortcut for this pattern called the render() function! The render() function will do the work of loading the template and provide the contexts when they are passed as arguments.

Our example above can be rewritten with the shortcut function like this:

from django.shortcuts import render
 
def home(request):
  context = {"name": "Junior"}
  return render(request, "app/home.html", context)
Note that we no longer need to import loader and HttpResponse when we use the render() function. The render() function takes the request object as its first argument, a template name as its second argument, and a dictionary as an optional third argument that passes the context variables to the template.












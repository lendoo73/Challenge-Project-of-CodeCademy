#### CRUD FUNCTIONALITY

# [Creating an Instance](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/creating-an-instance)

In this exercise, we will use the *Python shell* to create instances of models. 
The Python shell is a command-line tool that starts up a Python interpreter which we will use to execute CRUD functionality.

We can run the Python shell by using the following command in the command-line tool.
```
python3 manage.py shell
```
In order to work with our models in the Python shell we need to import them the same way we would in a Python file:
```py
>>> from app_name.models import ModelName
```
With our model imported, we can start creating instances (specific examples) of the model. 
Let’s say that we’re creating a website like Twitter that has a `Post` model with the fields `title` and `description`. 
To create an instance of our model we need to call our model and fill out the fields like so:
```py
>>> post_instance=Post(title="New", description="My Post")
```
Here, we start with a variable called `post_instance` that will store our instance. 
Then we used the `Post` model and provided the necessary arguments and values for the title and description fields. 
Note that while variables are not necessary to create instances, it gives us a nice way to refer to our created instances later on.

We’ve created our instance but we still need to save it to our database by calling `.save()` on the `post_instance` variable:
```py
>>> post_instance.save()
```
With our instance made, we should exit out of the shell. 
We can exit out of the Python shell by typing out the command `exit()`. 
In Windows we can press `ctrl` + `Z`. 
On Mac or Linux `ctrl` + `D`.

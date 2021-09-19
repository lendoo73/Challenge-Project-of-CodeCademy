#### CRUD FUNCTIONALITY

# [The `get()` and `get_or_create()` Method](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/the-get-and-get-or-create-method)

Yay, we’ve finished with the basics of CRUD! 
Now let’s get introduced to some useful methods, starting with `.get()`.

The [`.get()` method](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#get) 
returns an object that matches the arguments we give it. 
This method should mainly be used to look up values that are unique to return a single instance. 
If our query returns multiple objects we will get a [`.MultipleObjectsReturned` exception](https://docs.djangoproject.com/en/3.1/ref/exceptions/#multipleobjectsreturned). 
And if nothing matches, we’ll get a [`.DoesNotExist` exception](https://docs.djangoproject.com/en/3.1/ref/exceptions/#objectdoesnotexist). 
Here’s an example of the syntax:
```py
>>> unique_instance = ModelName.objects.get(name = "Ruqisa")
>>> unique_instance
<ModelName: ModelName object (10)>
```
In the example above, we called `.get()` with a `name = "Ruqisa"` argument and when we check the returned value, we get an instance. 
Even though we only used a single argument, we could’ve added as many arguments as there are fields.

Another method that gives even more functionality is the [`.get_or_create()` method](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#get-or-create).

What `.get_or_create()` does is look through the database for an object with the conditions that we provide. 
If an object fits our conditions it will return the object, otherwise, it will create the object hence its name `.get_or_create()`.

Let’s look at an example:
```py
>>> wanted_object = ModelName.objects.get_or_create(title = "example", content = "jango")
>>> wanted_object
(<ModelName: ModelName object (15)>, True)
```
The code above looks through our database for an object with the `title` of `"example"` and `content` of `"jango"`. 
Notice that we get a tuple back. 
The first element of the tuple is the object itself and the second element is a boolean (`True` if the object was just created, or `False` if the object was not just created). 
In this case, there was no model that has a `title = "example"` and `content = "jango"`. 
Hence we get back `(<ModelName: ModelName object (15)>, True)`.

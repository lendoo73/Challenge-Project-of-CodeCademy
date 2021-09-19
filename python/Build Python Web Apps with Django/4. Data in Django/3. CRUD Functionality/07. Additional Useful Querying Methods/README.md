#### CRUD FUNCTIONALITY
 
 # [Additional Useful Querying Methods](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/additional-useful-querying-methods)

Let’s look at some other common querying methods, like `.exclude()`.

The [`.exclude()` method](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#exclude) 
does the exact opposite of the `.get()` method. 
Instead of returning an object with matching arguments, it returns all objects that do **not** match the arguments.
```py
>>> not_trucks = ModelName.objects.exclude(title = "truck")
>>> not_trucks
<QuerySet [<ModelName: object (1)>, <ModelName: object (2)>]>
```
Another helpful method is the [`.order_by()` method](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#order-by). 
It allows us to return a list of objects based on a specified order. 
We can return based on the date posted, by ID number, etc.
```py
>>> ordered_by_id = modelName.objects.order_by("-pk")
>>> ordered_by_id
<QuerySet [<ModelName: object (2)>, <ModelName: object (1)>]>
```
Above, we created an `ordered_by_id` variable. 
In the variable we called a model and used the `.order_by()` method to sort by `"pk"`, or *primary key/ID*. 
We returned our instances by ID in descending order by adding the negative `"-"` sign in front of `"pk"`. 
Notice that we have `object(2)` appear before `object(1)`.

We can even return the objects randomly:
```py
>>> random_ordering = ModelName.objects.order_by("?")
```
This will return our objects ordered randomly every time.

There are many more useful query methods that we can look up in Django’s [documentation](https://docs.djangoproject.com/en/3.1/ref/models/querysets/).

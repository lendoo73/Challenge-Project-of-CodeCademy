#### CRUD FUNCTIONALITY

# [Reading Instances](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/reading-instances)

Being able to read instances of a model can give us more information about what’s stored in the database and the shape of our data. 
When we want to view all instances of a model, we can run the [`.all()` method](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#all) 
on the model like so:
```py
>>> every_instance = ModelName.objects.all()
```
Here we created a variable called `every_instance`. 
In the variable, we called a model followed by `.objects` followed by the `.all()` query method. 
This will return every instance of the model, which should look something like this:
```py
>>> every_instance
<QuerySet [<ModelName: object (1)>, <ModelName: object (2)>]>
```
Our code returns us a ***QuerySet***, a collection of objects from our database. 
In this QuerySet two instances, each instance associated with a number which is the instance’s ID number. 
We should also know that a QuerySet is indexable, meaning we can grab an instance by their index.
```py
>>> every_instance[0]
<ModelName: object (1)>
```
In the above code snippet, we referenced the variable `every_instance` and searched for the instance in the index position `0`. 
In the next line, we get returned the first instance in the QuerySet (`<ModelName: object (1)>`).

There’s also another way that we can return the first instance of a model using a query method using the `.first()` query method:
```py
>>> first_instance = ModelName.objects.first()
>>> first_instance
<ModelName: object (1)>
```
In our code snippet, we created a variable called `first_instance` where we called `ModelName.objects.first()`. 
Then, we referenced the variable `first_instance` and it returned us the very first instance created for that model.

The `.first()` and `.all()` method (or any other method) can be combined with other methods to make more complicated queries 
but we will get deeper into this as we progress throughout the lesson.

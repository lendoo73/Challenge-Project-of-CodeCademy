#### CRUD FUNCTIONALITY

# [Updating an Instance](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/updating-an-instance)

In the previous exercise, we learned how to view all instances of a model and individual instances. 
Now let’s learn how to update an instance’s field value.

Imagine we stored our first instance of a model in a variable called `first_instance`. 
To view one of its field’s values we can use dot notation:
```py
first_instance.name
```
Above, we’re accessing `first_instance`‘s `.name` field’s value. 
This would give us an output of the value like so:
```py
>>> first_instance.name
'Asiqur'
```
If we want to change the field’s value, we can reassign it to something else.
```py
>>> first_instance.name = "Ruqisa"
```
When we hit <kbd><b>Enter</b></kbd> the instance’s `name` field value will be changed to `"Ruqisa"`. 
If we type out `first_instance.name` again and hit <kbd><b>Enter</b></kbd> it will return an output value of `"Ruqisa"`.
```py
>>> first_instance.name
'Ruqisa'
```
Great! We were able to update the field value of our instance, but it’s still not saved into our database until we call the `.save()` method like so:
```py
>>> first_instance.save()
```

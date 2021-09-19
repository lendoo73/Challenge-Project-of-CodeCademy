#### CRUD FUNCTIONALITY

# [Deleting an Instance](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/deleting-an-instance)

So far we’ve learned how to create, read, update instances, now let’s learn how to delete instances.

We can delete an instance by using the `.delete()` method like so:
```py
>>> first_instance.delete()
```
This method will delete the instance stored in the `first_instance` variable from our database. 
We’ve deleted our instance, but what if we wanted to also delete everything that was related to that instance? 
This is where `.CASCADE` comes in, and it saves us a lot of time!

We’ve seen `.CASCADE` before when discussing foreign keys, so let’s dive a little deeper. 
We can think of `.CASCADE` like a domino effect, where one falling domino knocks down an entire row of dominos. 
Therefore, when we use `.CASCADE` to delete an object, any other object that has a reference to it also gets deleted. 
Imagine we have a Twitter account. 
When we delete our account, anything related to the account also gets deleted. 
Without this cascade effect, after we deleted our account, our post(s) would still be in the database!

`.CASCADE` needs to be implemented in our model itself and we need to provide the argument `on_delete = models.CASCADE` to any foreign key’s in our model. 
Let’s say we have a `Post` model that has a field listing a user instance as a foreign key from a `User` model.
```py
class Post(models.Model)
  users = models.ForeignKey(User, on_delete = models.CASCADE)
```
We have our foreign key but we also included `on_delete = models.CASCADE` as an argument. 
If a user gets deleted from the `User` model, all `Post` instances related to that user will also get deleted.

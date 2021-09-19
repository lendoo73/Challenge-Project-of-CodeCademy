#### CRUD FUNCTIONALITY

# [Reverse Relationships](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/reverse-relationships)

Let’s get a little deeper into querying two tables. 
In our previous exercise, we were able to access every `Answer` related to a `Question` because our `Answer` model held a foreign key to our `Question` model. 
What if we wanted to explore the other side of the relationship and use the `Question` model to query for all related `Answe`r instances? 
This query is called reverse relation, since that the relationship is now flipped, the table that’s doing the querying doesn’t contain a foreign key.

Suppose we have a variable called `question_instance` that stores an instance of our `Question` model. 
We can get the related `Answer` instances to that question instance by [using `_set`](https://docs.djangoproject.com/en/3.1/ref/models/relations/) 
like so.
```py
>>> question_instance.answer_set.all()
```
Above, we access the `.answer_set` property of the `question_instance`. 
By convention, the `_set` property is preceded by the lowercase name of the model. 
Notice that we use `.all()` at the end to access every `Answer` instance related to `question_instance`.

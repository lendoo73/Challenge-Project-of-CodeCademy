#### CRUD FUNCTIONALITY

# [Querying Two Tables](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/querying-two-tables)

Oftentimes, we need to work with different models at the same time since apps generally have more than a single model and their models often relate to each other. 
To gain more insight into how these models work together and what information they share, we should learn how to query two tables at the same time.

Remember, foreign keys can connect two tables together through a one-to-many relationship. 
For example, imagine if we have an `Answer` model and a `Question` model. 
A single `Question` can have many `Answer` instances. 
So the `Answer` model stores a foreign key of the `Question` model to its own table.

Now let’s say we want to return every `Answer` to a `Question`. 
We can use the [`.filter()` method](https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-specific-objects-with-filters) 
to look for every `Answer` instance related to a question instance. 
The first thing we need to do is capture a `Question` instance in a variable. 
For now, let’s say we have a variable called `question_instance` that holds the question `"Is blue a color?"`. 
Now in our `.filter()` method, we can provide the `question_instance` variable as an argument and get back matching results.
```py
>>> question_instance = Question.objects.get(question = "Is blue a color?") 
>>> Answer.objects.filter(question = question_instance)
<QuerySet [<Answer: No>, <Answer: Yes>, <Answer: It is a number>]>
```
Above, we used the `Answer` model and called the `.filter()` method with the argument `question = question_instance`. 
When we run the above query it will return a *QuerySet* with every `Answer` instance that’s associated with the `Question` instance `"Is blue a color?"`. 
We used a specific instance before to filter, but we can also use fields, like an ID. 
Django allows us to prepend `_id` to the name of the foreign key table to filter by ID, like so:
```py
>>> Answer.objects.filter(question_id = 3)
<QuerySet [<Answer: It is a number>]>
```
The above code will return every `Answer` instance related to the `Question` instance whose ID is `3`.

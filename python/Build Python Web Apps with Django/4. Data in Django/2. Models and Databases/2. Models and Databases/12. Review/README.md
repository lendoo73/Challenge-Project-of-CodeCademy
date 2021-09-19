#### MODELS AND DATABASES

# [Review](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/review)

Nice work, we’ve done a lot in this lesson and we’re going to get our databases populated soon!

In this lesson, we covered:
* A **schema** is a structure we design for the data in our application.
* A **model** is a Python class that contains characteristics and behavior using: attributes, metadata, and methods.
* Model **attributes** are implemented using Django field names and different field types.
* Django models can relate to other models. One way of showing this connection is to use a **foreign key**.
* Django **field types** accept optional keyword arguments based on key-value pairs such as `null`, `blank`, `choices`, `default`, and `primary_key`.
* Models can contain **metadata** using a nested `Meta` class and providing specific attributes.
* **Models** can have **methods** that are functions specific to that model. Some methods are inherited from the parent `Model` class.
* Django requires that we commit our models to the database via a **two-step migration procedure** with `makemigrations` and `migrate`.
* Django lets us **undo** one or more **migrations** by supplying the `migrate` command with a named migration.

Our models and database are now all set up and ready to accept and store information — time to Djump for Djoy!

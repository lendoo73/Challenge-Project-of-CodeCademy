#### MODELS AND DATABASES

# [Migrations - makemigrations](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/migrations-makemigration)

From when we first created our project, we’ve configured some database settings and let our project know about our app in **settings.py**. 
Now we need to let our database know about our models.

This step of setting the database to match the structure of the models is called [***migration***](https://docs.djangoproject.com/en/3.1/topics/migrations/). 
Remember, migrations are needed when we make changes to our models — and we’ve just made two new ones!

In Django, there are two steps necessary to make this migration happen:
1. Running `python3 manage.py makemigrations` to create a file with the instructions needed for our database to create the proper schemas.
2. Running `python3 manage.py migrate` to execute the instructions in our file to create the actual tables in our database.

We’ll first focus on `makemigrations`. 
Since we need to use **manage.py** to execute this step, we need to be in our root folder to execute:
```
python3 manage.py makemigrations
```
Using our hypothetical `Flower` and `Gardener` example, we should see something similar to:
```
Migrations for 'gardens':
  gardens/migrations/0001_initial.py
    - Create model Flower
    - Create model Gardener
```
We can also provide an additional argument after `makemigrations` and specify a chosen app’s models we want to commit. 
For instance, if we had two apps `Garden` and `FlowerShop` and we only wanted to commit the models for `Garden`, we could execute the command: 
`python3 manage.py makemigrations garden`.

The files created from this step live in the **migrations** folder within our app directory. 
Our first migration file would begin with **0001_initial.py**. 
We can refer to our migrations using the starting numbers, in this case, it has a migration name of `0001`.

It’s important that every time we need to make a change to the schema in our database we need to do this  `makemigrations` step! 
Subsequent migration files will increase the number at the beginning of the file. 
For example, the second migration will begin with **0002_xxxxx.py** and so forth.

We’ll run the [`makemigrations` step](https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-makemigrations) 
now and then follow up with the next step in the next exercise.

#### MODELS AND DATABASES

# [Creating a Model](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/creating-a-model)

We’ve thought through the schema and our database was set up by default when we first created our project. 
Time to create our models!

Every time we create a new app, Django provides us with a folder structure for our work which includes a file called **models.py** with the following starter code:
```py
from django.db import models
 
# Create your models here.
```
To create a model, we write a class, like so:
```py
class Flower(models.Model):
  ## Define attributes here
  pass
```
Notice that our model actually inherits from the `Model` parent class `django.db.models.Model` module. 
These models will later inform the database to use this schema to build its tables. 
In the example above, our database will know that incoming data records will contain attributes of our flowers, like perhaps, petal color, number of petals, average height, etc. 
For now, we’ve added the `pass` keyword to avoid any errors since Python doesn’t allow for empty classes.

Let’s now create our first models!

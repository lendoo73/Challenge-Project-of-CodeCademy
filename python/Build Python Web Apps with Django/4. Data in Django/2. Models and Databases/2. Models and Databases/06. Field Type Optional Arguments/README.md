#### MODELS AND DATABASES

# [Field Type Optional Arguments](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/field-type-optional-arguments)

We can continue to customize our models by supplying fields with options, that specify how data can be inserted into the database. 
Django provides [field option documentation](https://docs.djangoproject.com/en/3.1/topics/db/models/#field-options)
, which shows a huge list of these options. 
Let’s go over some common ones together!

One common option is `null` that can take on a value of `True` or `False`. 
This `null` option tells the database if a field can be left intentionally void of information. 
By default, Django sets `null = False`. 
However, we can override the default and set `null = True`. 
Here’s an example:
```py
class Flower(model.Model):
  petal_number = models.IntegerField(max_length = 20, null = True)
  # Other fields 
```
With the code above, when we create a `Flower` instance, we can set `petal_number` to `null`.

Another common option is `blank`, which is similar to `null`, but setting `blank` to `True` means a field doesn’t have to take anything, not even a `null` value. 
By default `blank` is `False`.
```py
class Flower(model.Model):
  nickname = models.CharField(max_length = 20, blank = True)
  # Other fields
```
Now, when we create a `Flower` instance, we can leave the `nickname` field blank.

The last one we’ll touch upon is `choices` which limits the input a field can accept. 
We can set `choices` by creating a list of tuples that contain 2 items: a key and a value. 
Take for example:
```py
class Flower(models.Model):
  COLOR_CHOICES = [
     ("R", "Red"),
     ("Y", "Yellow"),
     ("P", "Purple"),
     ("O", "Other"),
  ]
 
  color = models.CharField(max_length=1, choices=COLOR_CHOICES)
  # Other fields
```
For our `Flower` instance, we can specify its color with the limited choices provided — 
meaning our `color` field can only be assigned `"R"` (for `"Red"`), `"Y"` (for `"Yellow"`), 
or `"P"` (for `"Purple"`), or `"O"` (for `"Other"` from the `COLOR_CHOICES` list. 
With choices we know exactly what data we can accept from users.

We covered 3 options in this exercise, but remember, there are many more [field options](https://docs.djangoproject.com/en/3.1/topics/db/models/#field-options) 
to explore!

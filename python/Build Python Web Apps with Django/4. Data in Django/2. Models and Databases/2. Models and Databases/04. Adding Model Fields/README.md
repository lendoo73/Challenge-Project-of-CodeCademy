#### MODELS AND DATABASES
 # [Adding Model Fields](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/adding-model-fields)
 
As we mentioned, models are used to represent real-life objects. 
We can mimic and create object attributes in our models using *fields*. 
Fields have names and are assigned a type. 
For example, a `Flower` model can have a `petal_color` field that expects a string:
```py
class Flower(models.Model):
  petal_color = models.CharField()
```
Django uses specific *field types* to match the expected data with what will go into the database. 
Above, we used the [`.CharField()` type](https://docs.djangoproject.com/en/3.1/ref/models/fields/#charfield) 
to store a short string. 
We can continue to add to our model and include other attributes, like `petal_number`.
```py
class Flower(models.Model):
  petal_color = models.CharField()
  petal_number = models.IntegerField()
  # More attributes… 
```
Since we want `petal_number` to be a number, we used the `.IntegerField()` field type. 
Django provides a huge variety of field types for us to specify the data types of our model attributes, check out [the Field Types Documentation](https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types) 
to explore the entire list of possibilities!

We might also want to add constraints to our fields. 
For example, we might want our `petal_color` field to have a max length of 20 characters. 
We can supply an argument like so:
```py
class Flower(models.Model):
  petal_color = models.CharField(max_length = 20)
  petal_number = models.IntegerField(default = 0)
```
These arguments give us finer control over what data we want to include in our database. 
For `.CharField()` we used `max_length` to limit the number of acceptable characters to `20`. 
We can even set default values, like for `petal_number`, we set `default = 0` meaning if we didn’t provide a value for `petal_number` the value is automatically `0`.

Each field accepts different arguments, so make sure to check the [documentation](https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types).

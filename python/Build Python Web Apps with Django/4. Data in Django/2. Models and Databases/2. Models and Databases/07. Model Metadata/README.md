#### MODELS AND DATABASES

# [Model Metadata](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/model-metadata)

We’ve supplied our models with plenty of fields and data, but what about *metadata*? 
Let’s first define it.

[**Metadata**](https://docs.djangoproject.com/en/3.1/ref/models/options/#model-meta-options) 
is an optional entity within a model and it is anything that is not a field. 
Some helpful metadata can include how to order instances, create human-readable names, providing a database table name, and more.

To add metadata to a model, we’ll need to nest another `class` called `Meta` inside the model’s class definition. 
Let’s use metadata to order instances as an example:
```py
class Flower(models.Model):
  name = models.CharField(max_length=10)
  # All the other attributes
 
  class Meta:
    ordering = ["name"]
```
In this case, we created an attribute, `ordering` which takes a list of strings (`["name"]`) that determine the ordering. 
Later on, when we need to search for `Flower` instances, the database will return back a list with the list ordered by the `name` field. 
We can even reverse the order by adding a `-` in front of a string like `["-name"]`.

Other metadata work in a similar fashion. 
Let’s try adding a verbose human-readable name:
```py
class TropicalFlower(models.Model):
  # Fields and Methods
 
  class Meta:
    verbose_name = "tropical flower" 
```
Without setting this metadata, our model’s name would be `tropical_flower` by default, here we’ve assigned the verbose name to be `"tropical flower"`. 
While our change was subtle, we could provide even more detail to inform other developers about our model.

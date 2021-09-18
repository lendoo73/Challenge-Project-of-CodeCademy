#### MODELS AND DATABASES
# [Native Model Methods](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/native-model-methods)

We haven’t implemented *methods* yet to emulate any model behaviors. 
The properties we’ve created for our flowers describe what our flower **is** or **has**. 
They are like the nouns and adjectives that describe each flower. 
What we are missing though, and why modeling database data is so useful to begin with, are the **verbs**, the actions associated with our flowers. 
These are called methods. 
Methods are functions defined in our model that describe the behaviors and actions of our model. 
If properties are what our models **are**, then methods are what our models **do**. 
For example, our flower might `bloom()` and `grow()`.

In Python classes, which Django uses to create models, there are built-in methods we can override like the [`__str__` method](https://docs.djangoproject.com/en/3.1/ref/models/instances/#str). 
All this means is we are creating a method using the same name as the built-in one. 
This is how we, the programmer, take control, or “override”, the default behavior of the built-in version:
```py
class Gardener(models.Model):
  name = models.CharField(max_length = 30)
 
  def __str__(self):
    return self.name
```
Methods always require the first parameter to be `self`, then we can provide other optional parameters and add logic within the method body. 
In the next lesson, we’ll learn how useful overriding `__str__` is when we need to retrieve instances of models from our database — by default, 
if we didn’t override `__str__` printing our instances would generate output that’s hard to read like:
```
<QuerySet [<Gardener:>,<Gardener:>,<Gardener:>....]
```
But with our overridden `__str__` method, we’ll get more helpful information, in this case, we’re returning the `Gardener` instance’s name:
```
<QuerySet [<Gardener: Linnaeus>,<Gardener: Mendel>, <Gardener: Carver >....]
```

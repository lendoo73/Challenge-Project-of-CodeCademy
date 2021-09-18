#### MODELS AND DATABASES

# [Custom Model Methods](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/custom-model-methods)

In addition to overriding native methods, we can define our own custom methods!

We can do something simple like returning a boolean:
```py
class Flower(models.Model):
  has_sunlight = models.BooleanField(default = True)
  has_water = models.BooleanField(default = True)
 
  def can_grow(self):
    return self.has_sunlight and self.has_water
```
Above, we defined our custom `.can_grow()` method that checks if the instance’s `.has_sunlight` and `.has_water` fields are `True`. 
Notice that even for custom methods, we need to provide the first parameter as `self`. 
We can also provide additional parameters as needed.

Here’s another example that returns a string:
```py
class Gardener(models.Model):
  years_experience = models.IntegerField()
 
  def identify_flower(self, flower):
    return f"I've studied flowers for {self.years_experience}. I believe this flower is {flower.name} and is found in {flower.native_env}." 
```
In this case, we’ve added a second parameter to our method, a `flower` instance, and returned a string. 
Both methods do different things but both help emulate real-life behaviors. 
Check out [Django documentation](https://docs.djangoproject.com/en/3.1/topics/db/models/#model-methods) 
for more insight!

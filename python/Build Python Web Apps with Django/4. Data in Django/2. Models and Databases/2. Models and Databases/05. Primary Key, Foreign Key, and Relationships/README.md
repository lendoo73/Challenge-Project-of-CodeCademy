#### MODELS AND DATABASES

# [Primary Key, Foreign Key, and Relationships](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/primary-key-foreign-key-and-relationships)

Later on, we’ll use these models to create instances (specific model objects) in our database. With a Flower model, we could create instances with characteristics of flowers like a rose, a sunflower, or a daisy. Instances then correspond to rows, or records, in our database.

We’d also need our instances to have a unique ID to help us keep track of each one. These IDs are called primary keys and Django helps us automatically create these unique IDs by incrementing by 1 each time. For example, if our first Flower instance is rose, it would have a primary key/ID of 1. The second instance, sunflower, a primary key of 2 — then maybe a daisy with a primary key of 3, and so forth:

name	ID
rose	1
sunflower	2
daisy	3
In our apps, we often create multiple models that relate to each other in some way. For our example Flower model, we could have a gardener tend to flowers! This means we need to create another model called Gardener:

class Gardener(models.Model):
  first_name = models.CharField(max_length=20)
  years_experience = models.IntegerField()
Now the question is how do we show this relationship between Flower and Gardener? Well, let’s say that a Gardener instance can tend to multiple Flower instances, but a Flower instance can only have a single Gardener. This means we have a One to Many relationship, one Gardener for multiple Flowers. Conversely, Flowers have a Many to One relationship with a Gardener.

To make this connection known, we need to supply Flower with a foreign key of a Gardner, i.e. the Flower instances know which Gardener instance takes care of it.

# Garden has a one-to-many relationship with Flower
class Gardener(models.Model):
  first_name = models.CharField(max_length=20)
  years_experience = models.IntegerField()
 
# Flower has a many-to-one relationship with Gardener
class Flower(models.Model):
  petal_color = models.CharField(max_length=10)
  petal_number = models.IntegerField()
  gardener = models.ForeignKey(Gardener, on_delete=models.CASCADE) 
Notice that we added the gardener field using models.ForeignKey() and with arguments. The first argument is Gardener because that’s the model we want this foreign key to come from. Then we add on_delete=models.CASCADE to let Django know to delete the Flower instance if its connected Gardener instance is deleted. We’ll cover more about on_delete in a later lesson — for more information check out Django’s arguments documentation.

Hypothetically, we could even supply Gardener with a foreign key as well if we wanted to link Gardener to another model, like a Garden for example! These foreign keys tell the database that a one-to-many relationship exists and the direction of this relationship. There are other types of relationships, but let’s implement a one-to-many relationship with our own models!

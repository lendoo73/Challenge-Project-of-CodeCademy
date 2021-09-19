#### CRUD FUNCTIONALITY

# [Review](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-crud-functionality/exercises/review)

PHEW! 
That was a lot to take in. 
Let’s go over a quick summary of what we’ve learned so far.
* **CRUD** is the four basic functions of a database. CRUD stands for Create, Read, Update and Delete.
* A new instance of a model can be created by calling the model then filling out the fields of the model. The instance can be saved to the database by using **`.save()`**.
* We can view all queries of a model by using the **`.all()`** method.
* We can **update** an instance of a model by reassigning a field value and saving the instance.
* We can delete an instance by using the **`.delete()`** method.
* The **`.get()`** method returns an object that matches the argument(s)parameters we give it.
* The **`.get_or_create()`** method looks through the database and looks for any object with the conditions that we provide. 
If it does find an object with our conditions it will return the object if not it will create the object.
* The **`.exclude()`** method returns an object that does not match the argument we give it.
* We can use the **`.order_by()`** method to return objects in any order we like.
* The **`.filter()`** method can be used to query two tables. The `.filter()` method can take in a foreign key and return an instance associated with that foreign key.
* We can query using the reverse relation by **`appending _set`** to a model’s name to find related model instances.

Congrats! You’ve made it through and learned so much. 
Now you can use your knowledge to dig deeper into how to interact with the database!

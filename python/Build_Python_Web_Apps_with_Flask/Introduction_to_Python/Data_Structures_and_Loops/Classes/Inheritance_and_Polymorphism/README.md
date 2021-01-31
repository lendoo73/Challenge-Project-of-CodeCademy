# Inheritance and Polymorphism

## [Inheritance](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/flask-python-data-structures-loops/modules/learn-python3-classes/lessons/inheritance-and-polymorphism/exercises/inheritance)

Classes are designed to allow for more code reuse, but what if we need a class that looks a lot like a class we already have? 
If the bulk of a class’s definition is useful, but we have a new use case that is distinct from how the original class was used, we can inherit from the original class. 
Think of inheritance as a remix — it sounds a lot like the original, but there’s something… different about it.
```
class User:
  is_admin = False
  def __init__(self, username)
    self.username = username
 
class Admin(User):
  is_admin = True
```
Above we defined `User` as our base class. 
We want to create a new class that inherits from it, so we created the subclass `Admin`. 
In the above example, `Admin` has the same constructor as `User`. 
Only the class variable `is_admin` is set differently between the two.

Sometimes a base class is called a parent class. 
In these terms, the class inheriting from it, the subclass, is also referred to as a child class.

## [Exceptions](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/flask-python-data-structures-loops/modules/learn-python3-classes/lessons/inheritance-and-polymorphism/exercises/exceptions)

There’s one very important family of class definitions built in to the Python language. 
An Exception is a class that inherits from Python’s `Exception` class.

We can validate this ourselves using the `issubclass()` function. 
**`issubclass()`** is a Python built-in function that takes two parameters. 
`issubclass()` returns `True` if the first argument is a subclass of the second argument. 
It returns `False` if the first class is not a subclass of the second. 
`issubclass()` raises a `TypeError` if either argument passed in is not a class.
```
issubclass(ZeroDivisionError, Exception)
# Returns True
```
Above, we checked whether `ZeroDivisionError`, the exception raised when attempting division by zero, is a subclass of `Exception`. 
It is, so issubclass returns `True`.

Why is it beneficial for exceptions to inherit from one another? 
Let’s consider an example where we create our own exceptions. 
What if we were creating software that tracks our kitchen appliances? 
We would be able to design a suite of exceptions for that need:
```
class KitchenException(Exception):
  """
  Exception that gets thrown when a kitchen appliance isn't working
  """
 
class MicrowaveException(KitchenException):
  """
  Exception for when the microwave stops working
  """
 
class RefrigeratorException(KitchenException):
  """
  Exception for when the refrigerator stops working
  """
```
In this code, we define three exceptions. 
First, we define a `KitchenException` that acts as the parent to our other, specific kitchen appliance exceptions. 
`KitchenException` subclasses `Exception`, so it behaves in the same way that regular `Exceptions` do. 
Afterward we define `MicrowaveException` and `RefrigeratorException` as subclasses.

Since our exceptions are subclassed in this way, we can catch any of `KitchenException`‘s subclasses by catching `KitchenException`. For example:
```
def get_food_from_fridge():
  if refrigerator.cooling == False:
    raise RefrigeratorException
  else:
    return food
 
def heat_food(food):
  if microwave.working == False:
    raise MicrowaveException
  else:
    microwave.cook(food)
    return food
 
try:
  food = get_food_from_fridge()
  food = heat_food(food)
except KitchenException:
  food = order_takeout()
```
In the above example, we attempt to retrieve food from the fridge and heat it in the microwave. 
If either `RefrigeratorException` or `MicrowaveException` is raised, we opt to order takeout instead. 
We catch both `RefrigeratorException` and `MicrowaveException` in our try/except block because both are subclasses of `KitchenException`.

Explore [Python’s exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) 
in the Python documentation!

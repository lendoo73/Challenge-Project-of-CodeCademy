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

## [Overriding Methods](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/flask-python-data-structures-loops/modules/learn-python3-classes/lessons/inheritance-and-polymorphism/exercises/overriding-methods)

In Python, all we have to do to override a method definition is to offer a new definition for the method in our subclass.

An overridden method is one that has a different definition from its parent class.

## [Super()](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/flask-python-data-structures-loops/modules/learn-python3-classes/lessons/inheritance-and-polymorphism/exercises/super)

Sometimes we want to add some extra logic to the existing method. 
In order to do that we need a way to call the method from the parent class. 
Python gives us a way to do that using `super()`.

**`super()`** gives us a proxy object. 
With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). 
We call the required function as a method on `super()`:
```
class Sink:
  def __init__(self, basin, nozzle):
    self.basin = basin
    self.nozzle = nozzle
 
class KitchenSink(Sink):
  def __init__(self, basin, nozzle, trash_compactor = None):
    super().__init__(basin, nozzle)
    if trash_compactor:
      self.trash_compactor = trash_compactor
```
Above we defined two classes. 
First, we defined a `Sink` class with a constructor that assigns a rinse basin and a sink nozzle to a `Sink` instance. 
Afterwards, we defined a `KitchenSink` class that inherits from `Sink`. 
`KitchenSink`‘s constructor takes an additional parameter, a `trash_compactor`. 
`KitchenSink` then calls the constructor for `Sink` with the `basin` and `nozzle` it received using the `super()` function, with this line of code:
```
super().__init__(basin, nozzle)
```
This line says: “call the constructor (the function called `__init__()`) of the class that is this class’s parent class.” 
In the example given, `KitchenSink`‘s constructor calls the constructor for `Sink`. 
In this way, we can override a parent class’s method to add some new functionality (like adding a `trash_compactor` to a sink), while still retaining the behavior of the original constructor (like setting the `basin` and `nozzle` as instance variables).

## [Interfaces](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/flask-python-data-structures-loops/modules/learn-python3-classes/lessons/inheritance-and-polymorphism/exercises/interfaces)

You may be wondering at this point why we would even want to have two different classes with two differently implemented methods to use the same method name. 
This style is especially useful when we have an object for which it might not matter which class the object is an instance of. 
Instead, we’re interested in whether that object can perform a given task.

If we have the following code:
```
class Chess:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_chess_pieces()
 
  def play(self):
    print("Playing chess!")
 
class Checkers:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_checkers_pieces()
 
  def play(self):
    print("Playing checkers!")
```
In the code above we define two classes, `Chess` and `Checkers`. 
In `Chess` we define a constructor that sets up the board and pieces, and a `.play()` method. 
`Checkers` also defines a `.play()` method. 
If we have a `play_game()` function that takes an instance of `Chess` or `Checkers`, it could call the `.play()` method without having to check which class the object is an instance of.
```
def play_game(chess_or_checkers):
  chess_or_checkers.play()
 
chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()
 
for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)
"""
Prints out the following:
Playing chess!
Playing checkers!
Playing chess!
"""
```
In this code, we defined a `play_game` function that could take either a `Chess` object or a `Checkers` object. 
We instantiate a few objects and then call `play_game` on each.

When **two classes have the same method names and attributes**, we say they implement the **same interface**. 

An interface in Python usually refers to the names of the methods and the arguments they take. 
Other programming languages have more rigid definitions of what an interface is, but it usually hinges on the fact that different objects from different classes can perform the same operation (even if it is implemented differently for each class).




* `hasattr(object, "attribute")` will return `True` if an object has a given attribute and `False` otherwise.
  * *object*: the object we are testing to see if it has a certain attribute
  * *attribute*: name of attribute we want to see if it exists
* `getattr(object, "attribute", default)` will return the value of a given object and attribute. 
  * *object*: the object whose attribute we want to evaluate
  * *attribute*: name of attribute we want to evaluate
  * *default*: the value that is returned if the attribute does not exist (this parameter is **optional**)

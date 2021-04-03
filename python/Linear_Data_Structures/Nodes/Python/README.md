#### NODES: PYTHON
# [Nodes Python Introduction](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-nodes-python/exercises/python-nodes-intro)
We will use a basic node that contains data and one link to another node. 
The node’s data will be specified when creating the node and immutable (can’t be updated). 
The link will be optional at initialization and can be updated.

Remember that at the end of a node path, the link to the next node is null because there are no more nodes left. 
In Python, this means it will be set to `None`.

# [Nodes Python Getters](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-nodes-python/exercises/python-nodes-getters)
We need methods to access the data and link within the node. 
For this, we will use two getters, `.get_value()` and `.get_link_node()`.

These should each return their corresponding value on the `self` object.

# [Nodes Python Setter](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-nodes-python/exercises/python-nodes-setter)
We are only allowing the value of the node to be set upon creation. 
However, we want to allow updating the link of the node. 
For this, we will use a setter to modify the `self.link_node` attribute.

The method should be called `.set_link_node()` and should take `link_node` as an argument. 
It should then update the `self.link_node` attribute as appropriate.

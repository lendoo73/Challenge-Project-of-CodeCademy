#### LINKED LISTS: PYTHON
# [Node Implementation](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-linked-lists-python/exercises/linked-lists-python-node)
Let’s implement a linked list in Python. 
As you might recall, each linked list is a sequential chain of nodes. 
So before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to build our data containers.

Remember that a node contains two elements:
* data
* a link to the next node
```
class Node():
  
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node
```
# [Linked List Implementation](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-linked-lists-python/exercises/linked-lists-python-list-i)
With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a variety of methods can be defined.

For our use, we want to be able to:
* get the head node of the list (it’s like peeking at the first item in line): `get_head_node()`
* add a new node to the beginning of the list: `insert_beginning()`
* print out the list values in order: `stringify_list()`
* remove a node that has a particular value: `remove_node()`

#### TREES: PYTHON

# [Trees Introduction](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-intro)

Before we start building (planting?) our trees, let’s do a quick inventory of what we’ll need in our Python implementation. 
We’re going to make the class `TreeNodes`.

`TreeNodes`:
* have a value
* have a reference to zero or more other `TreeNodes`
* can add a node as a child
* can remove a child
* can traverse (or travel through) connected nodes

# [Tree Implementation I: Planting Seeds](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-node-i)

Let’s start by defining our TreeNode class. 
We’ll begin with having our node store a value, and additional functionality can be layered on in the following exercises.
```python
class TreeNode:
  def __init__(self, value):
    print("initializing node…")
    self.value = value

seed = TreeNode("Csaba")
```

# [Tree Implementation II: Think of the Children](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-node-ii)

Trees are all about data hierarchy, and we need a parent-child relationship to make that work.

To review: child nodes are held as references by another instance of `TreeNode`, known as the parent node.
```python
parent = TreeNode('CEO')
child = TreeNode('Executive Assistant')
print(parent.children)
# []
parent.add_child(child)
print(parent.children)
# [child]
```

We’ll store the references to child nodes in a Python list and define an `add_child` method on our `TreeNode` class which will add nodes to that list.

Modify our `__init__()`
```python
  def __init__(self, value):
    self.value = value
    self.children = []
```
Define `add_child`
```python
  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)
```

# [Tree Implementation III: Pruning](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-iii)

Let’s explore how to remove nodes from a tree. 
Remember, child nodes are held in a list within the parent node. 
To remove a child, we need to remove that node from the list.

We want the following functionality:
```python
print(root.children)
# [child_a, child_b, child_c]
root.remove_child(child_b)
print(root.children)
# [child_a, child_c]
```
* Call `.remove_child` on a specific node.
* Pass another node as an argument
* Remove from `.children` any nodes which match the argument node.

Define a new method remove_child:
```python
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    new_children = []
    for child in self.children:
      if child != child_node:
        new_children.append(child)
    self.children = new_children
```

# [Tree Implementation III.a: Tuning the Pruning](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-iii-a)

Trees are an abstract idea that we’re making concrete in Python. 
When implementing these abstract data structures, it’s important to leverage the features of your language.

Let’s refactor `.remove_child()` to use Python’s list comprehension. 
As a quick refresher on list comprehension:
```python
nums = [1, 2, 3, 4, 5]
evens = [num for num in nums if num % 2 == 0]
# [2, 4]
```
```python
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children if child != child_node]
```

# [Tree Implementation IV: Traversing](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-iv)

Our implementation has covered adding and removing nodes. 
Let’s expand the functionality and add the ability to move through connected nodes.

Tree traversal is a standard operation for finding nodes with a specific value or printing all the nodes available in a tree.

We’d like to do the following:
```python
root = TreeNode('Founder')
child_a = TreeNode('VP of Bananas')
child_b = TreeNode('Executive Assistant')
 
root.add_child(child_a)
root.add_child(child_b)
 
root.traverse()
# prints "Founder", "VP of Bananas", "Executive Assistant"
```
Define a traverse method:
```python
  def traverse(self):
    print(self.value)
    for child in self.children:
      print(child.value)
```

# [Tree Implementation V: Traversing Root to Leaf](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-v)

Our implementation of tree traversal has a slight hiccup. 
Trees grow many levels deep, but we’ve only accounted for one parent-child relationship.

How is this a problem?
```python
root = TreeNode('Founder')
child_a = TreeNode('VP of Bananas')
child_b = TreeNode('Executive Assistant')
child_c = TreeNode('Banana R & D')
 
# adding children to the root
root.add_child(child_a)
root.add_child(child_b)
 
# assigning child_c to child_a creates an additional level in the tree
child_a.add_child(child_c)
 
root.traverse()
# prints "Founder", "VP of Bananas", "Executive Assistant"
```

“VP of Bananas” is a child to “Founder”, and a parent to “Banana R & D”. 
`.traverse()` only goes one level deep which leaves out “Banana R & D”. 
Pull on your gardening gloves and let’s fix that!
```python
  def traverse(self):
    print("Traversing...")
    nodes_to_visit =[self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children
```

# [Tree Review](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-les/exercises/trees-review)

* Trees are a Python class called `TreeNode`.
* A `TreeNode` has two properties, `value` and `children`.
* Nodes hold any type of data inside `value`.
* `children` is a list, which can be empty or hold other instances of `TreeNode`.
* We add to `children` by using the list method `.append`.
* We remove from `children` by filtering the list.

This implementation will come in handy for a variety of algorithms in the future.

# [`depth()`](https://www.codecademy.com/courses/learn-recursion-python/lessons/iteration-recursion-python/exercises/iteration-recursion-python-depth)

[Binary trees](https://en.wikipedia.org/wiki/Binary_tree), trees which have at most two children per node, are a useful data structure for organizing hierarchical data.

It’s helpful to know the depth of a tree, or how many levels make up the tree.
```
# first level
root_of_tree = {"data": 42}
# adding a child - second level
root_of_tree["left_child"] = {"data": 34}
root_of_tree["right_child"] = {"data": 56}
# adding a child to a child - third level
first_child = root_of_tree["left_child"]
first_child["left_child"] = {"data": 27}
```
Here’s an iterative algorithm for counting the depth of a given tree.

We’re using Python dictionaries to represent each tree node, with the key of `"left_child"` or `"right_child"` referencing another tree node, or `None` if no child exists.
```
def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result
 
two_level_tree = {
"data": 6, 
"left_child":
  {"data": 2}
}
 
four_level_tree = {
"data": 54,
"right_child":
  {"data": 93,
   "left_child":
     {"data": 63,
      "left_child":
        {"data": 59}
      }
   }
}
 
 
depth(two_level_tree)
# 2
depth(four_level_tree)
# 4
```
This algorithm will visit each node in the tree once, which makes it a linear runtime, `O(N)`, where `N` is the number of nodes in the tree.

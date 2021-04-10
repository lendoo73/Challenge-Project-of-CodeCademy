#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [List Rotation: Indices](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-rotate-indices)

Optimizing a solution means reducing the **memory required (space complexity)**, or reducing the number of instructions the computer must execute (**time complexity**).

Sometimes this means entirely rethinking the approach to a question and it’s always meant to be a difficult task.

In the last exercise we created a new list using the slice operator. 
This requires `O(N)` space, because a new list is made with **copies of each value**, and **`O(N)`** time because **every value is visited** while copying. 
`N` represents the number of values in the list.

We need to do better than `O(N)`.

For time complexity, there’s not much we can do. 
Rotations could encompass the list, requiring us to iterate approximately `N` times.

For space complexity, we can optimize by constructing ***in-place solutions***, meaning **we don’t create any additional data structures for storing values**.

**Single variable declarations** are considered `O(1)`, or **constant space**, because we’re not allocating memory in relation to the input.

This example function adds `"!"` to each string in a list.
```python
def constant_space(list_of_strings):
  # variable the same regardless of input
  exclamation = "!"
  for element in list_of_strings:
    element += exclamation
 
  # input mutated but no more space used
  return list_of_strings
 
def linear_space(list_of_strings):
  exclamation_list = [] # new structure
  exclamation = "!"
 
  for element in list_of_strings:
    # adding a new value each loop
    exclamation_list.append(element + exclamation)
 
  # holds as many new values as the input!
  return exclamation_list   
```
Given a list and a positive integer, return the same list “rotated” a number of times that match the input integer. This time, we’ll rotate the list backward and use O(1) space.

list = ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 1)
# ['b', 'c', 'd', 'e', 'f', 'a']
rotate(list, 4)
# ['e', 'f', 'a', 'b', 'c', 'd']

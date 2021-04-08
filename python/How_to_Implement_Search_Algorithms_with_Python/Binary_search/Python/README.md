#### BINARY SEARCH: PYTHON

# [Recursive Binary Search: Base Case](https://www.codecademy.com/courses/search-algorithms/lessons/binary-implementation/exercises/recursive-binary)

Binary search is an efficient algorithm for finding values in a sorted data-set.

**Check the middle value of the dataset.**
* If this value matches our target we return the target value index.
* If the middle value is greater than our target
  * Begin at step 1 using the left half of the list.
* If the middle value is less than our target
  * Begin at step 1 using the right half of the list.

As an added challenge, we are going to use a recursive approach. 
When using recursion, we always want to think of the problem in two ways: the base case and the recursive step.

We have two base cases for this algorithm:
* We found the value and return its index
* We didn’t find the value because the list is empty!

In order to reach the base case of an empty list, we’ll need to remove an element at each recursive call…

# [Recursive Binary Search: Review and Refactor](https://www.codecademy.com/courses/search-algorithms/lessons/binary-implementation/exercises/recursive-binary-4)

1. We know our inputs will be sorted, which helps us make assertions about where to search for values.
2. We divide the list in half and compare our target value with the middle element.
3. If they match, we return the index
4. If they don’t match, we begin again at the first step with the appropriate half of the original list.
5. When the list is empty, the target is not found.

Our original solution solved the problem of reducing the sorted input list by making a smaller copy of the list.

This is wasteful! At each recursive call we’re copying `N/2` elements where `N` is the length of the sorted list.

We can do better by using pointers instead of copying the list. 
Pointers are indices stored in a variable that mark the beginning and end of a list:
```Python
vehicles = ["car", "jet", "camel", "boat"]
start_of_list = 0
end_of_list = len(vehicles)
# 4
 
vehicles[start_of_list : end_of_list]
# ["car", "jet", "camel", "boat"]
 
middle_of_list = len(vehicles) // 2
# 2
 
vehicles[start_of_list : middle_of_list]
# ["car", "jet"]
vehicles[middle_of_list : end_of_list]
# ["camel", "boat"]
 
# This example copies the list to show what portion is covered
# We won't need to copy in the algorithm!
```
With pointers, we’ll track which sub-list we’re searching within the original input and there’s no need for copying.

Our overall strategy is the same, but we’ll need to change the following sections:

binary_search() has two parameters
It should have four
Our base case checks for an empty list
It should check whether the pointers indicate an empty sub-list
Our recursive calls use copied sub-lists
They should update the pointers to indicate which portion of the list we’re searching.
Our “right-half” recursive calls do some arithmetic.
That’s no longer necessary!

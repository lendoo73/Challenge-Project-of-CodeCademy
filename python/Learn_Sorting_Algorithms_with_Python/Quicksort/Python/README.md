#### QUICKSORT: PYTHON

# [Quicksort Introduction](https://www.codecademy.com/courses/sorting-algorithms/lessons/quicksort-python/exercises/quicksort-python-intro)

Quicksort is an efficient way of sorting a list of values by partitioning the list into smaller sub-lists based on comparisons with a single “pivot” element.

Our algorithm will be recursive, so we’ll have a base case and an inductive step that takes us closer to the base case. 
We’ll also sort our list in-place to keep it as efficient as possible.

Sorting in place means we’ll need to keep track of the sub-lists in our algorithm using pointers and swap values inside the list rather than create new lists.

We’ll use pointers a lot in this algorithm so it’s worth spending a little time practicing. 
Pointers are indices that keep track of a portion of a list. 
Here’s an example of using pointers to represent the entire list:
```python
my_list = ['pizza', 'burrito', 'sandwich', 'salad', 'noodles']
start_of_list = 0
end_of_list = len(my_list) - 1
 
my_list[start_of_list : end_of_list + 1]
# ['pizza', 'burrito', 'sandwich', 'salad', 'noodles']
```
Now, what if we wanted to keep `my_list` the same, but make a sub-list of only the first half?
```python
end_of_half_sub_list = len(my_list) // 2
# 2
 
my_list[start_of_list : end_of_half_sub_list + 1]
# ['pizza', 'burrito', 'sandwich']
```
Finally, let’s make a sub-list that excludes the first and last elements…
```python
start_of_sub_list = 1
end_of_sub_list = len(my_list) - 2
 
my_list[start_of_sub_list : end_of_sub_list]
# ['burrito', 'sandwich', 'salad']
```
We’ll use two pointers, `start` and `end` to keep track of sub-lists in our algorithm.
```python
def quicksort(list, start, end):
  # base case:
  if start >= end: return

  # recursive step:
  print(list[start])
  start += 1
  quicksort(list, start, end)
```

# [Pickin' Pivots](https://www.codecademy.com/courses/sorting-algorithms/lessons/quicksort-python/exercises/quicksort-python-pivots)

Quicksort works by selecting a pivot element and dividing the list into two sub-lists of values greater than or less than the pivot element’s value. 
This process of “partitioning” the list breaks the problem down into two smaller sub-lists.

For the algorithm to remain efficient, those sub-lists should be close to equal in length. 
Here’s an example:
```python
[9, 3, 21, 4, 50, 8, 11]
# pick the first element, 9, as the pivot
# "lesser_than_list" becomes [3, 4, 8]
# "greater_than_list" becomes [21, 50, 11]
```
In this example the two sub-lists are equal in length, but what happens if we pick the first element as a pivot in a sorted list?
```python
[1, 2, 3, 4, 5, 6]
# pick the first element, 1, as the pivot
# "lesser_than_list" becomes []
# "greater_than_list" becomes [2,3,4,5,6]
```
Our partition step has produced severely unbalanced sub-lists! 
While it may seem silly to sort an already sorted list, this is a common enough occurrence that we’ll need to make an adjustment.

We can avoid this problem by randomly selecting a pivot element from the list each time we partition. 
The benefit of random selection is that no particular data set will consistently cause trouble for the algorithm! 
We’ll then swap this random element with the last element of the list so our code consistently knows where to find the pivot.
```python
# use randrange to produce a random index
from random import randrange

def quicksort(list, start, end):
  # base case:
  if start >= end:
    return list
  
  # recursive step:
  pivot_idx = randrange(start, end)

  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = pivot_element, list[end]

  print(list[start])
  start += 1

  return quicksort(list, start, end)
```

# [Partitioning Party](https://www.codecademy.com/courses/sorting-algorithms/lessons/quicksort-python/exercises/quicksort-python-partition)

We need to partition our list into two sub-lists of greater than or smaller than elements, and we’re going to do this “in-place” without creating new lists. 
Strap in, this is the most complex portion of the algorithm!

Because we’re doing this in-place, we’ll need two pointers. 
One pointer will keep track of the “lesser than” elements. 
We can think of it as the border where all values at a lower index are lower in value to the pivot. 
The other pointer will track our progress through the list.

Let’s explore how this will work in an example:
```python
[5, 6, 2, 3, 1, 4]
# we randomly select "3" and swap with the last element
[5, 6, 2, 4, 1, 3]
 
# We'll use () to mark our "lesser than" pointer
# We'll use {} to mark our progress through the list
 
[{(5)}, 6, 2, 4, 1, 3]
# {5} is not less than 3, so the "lesser than" pointer doesn't move
 
[(5), {6}, 2, 4, 1, 3]
# {6} is not less than 3, so the "lesser than" pointer doesn't move
 
[(5), 6, {2}, 4, 1, 3]
# {2} is less than 3, so we SWAP the values...
[(2), 6, {5}, 4, 1, 3]
# Then we increment the "lesser than" pointer
[2, (6), {5}, 4, 1, 3]
 
[2, (6), 5, {4}, 1, 3]
# {4} is not less than 3, so the "lesser than" pointer doesn't move
 
[2, (6), 5, 4, {1}, 3]
# {1} is less than 3, so we SWAP the values...
[2, (1), 5, 4, {6}, 3]
# Then we increment the "lesser than" pointer
[2, 1, (5), 4, {6}, 3]
 
# We've reached the end of the non-pivot values
[2, 1, (5), 4, 6, {3}]
# Swap the "lesser than" pointer with the pivot...
[2, 1, (3), 4, 6, {5}]
```
We have successfully partitioned this list. 
Note that the “sub-lists” are not necessarily sorted, we’ll need to recursively run the algorithm on each sub-list, but the pivot has arrived at the correct location within the list.
```python
from random import randrange

def quicksort(list, start, end):
  # base case:
  if start >= end:
    return list
  
  # recursive step:
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  lesser_than_pointer = start
  
  for idx in range(start, end):
    if list[idx] < pivot_element:
      list[lesser_than_pointer], list[idx] = list[idx], list[lesser_than_pointer]
      lesser_than_pointer += 1

  list[lesser_than_pointer], list[end] = list[end], list[lesser_than_pointer]

  print(list[start])
  start += 1
  
  return quicksort(list, start, end)
```

# [Recurse, Rinse, Repeat](https://www.codecademy.com/courses/sorting-algorithms/lessons/quicksort-python/exercises/quicksort-python-recurse)

We’ve partitioned the list once, but we need to continue partitioning until the base case is met.

Let’s revisit our example from the previous exercise where we had finished a single partition step:
```python
# the pivot, 3, is correctly placed
whole_list = [2, 1, (3), 4, 6, 5]
 
less_than_pointer = 2
start = 0
end = len(whole_list) - 1
# start and end are pointers encompassing the entire list
# pointers for the "lesser than" sub-list
left_sub_list_start = start
left_sub_list_end = less_than_pointer - 1
 
lesser_than_sub_list = whole_list[left_sub_list_start : left_sub_list_end]
# [2, 1]
 
# pointers for the "greater than" sub-list
right_sub_list_start = less_than_pointer + 1
right_sub_list_end = end
greater_than_sub_list = whole_list[right_sub_list_start : right_sub_list_end]
# [4, 6, 5]
```
The key insight is that we’ll recursively call quicksort and pass along these updated pointers to mark the various sub-lists. 
Make sure you’re excluding the index that stores the newly placed pivot value or we’ll never hit the base case!
```python
from random import randrange

def quicksort(list, start, end):
  # base case:
  if start >= end:
    return
  
  # recursive step:
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]

  # swap random element with last element in sub-listay
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  # Call quicksort on the "left" and "right" sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)
```

# [Quicksort Review](https://www.codecademy.com/courses/sorting-algorithms/lessons/quicksort-python/exercises/quicksort-python-review)

1. We established a base case where the algorithm will complete when the start and end pointers indicate a list with one or zero elements
2. If we haven’t hit the base case, we randomly selected an element as the pivot and swapped it to the end of the list
3. We then iterate through that list and track all the “lesser than” elements by swapping them with the iteration index and incrementing a lesser_than_pointer.
4. Once we’ve iterated through the list, we swap the pivot element with the element located at lesser_than_pointer.
5. With the list partitioned into two sub-lists, we repeat the process on both halves until base cases are met.

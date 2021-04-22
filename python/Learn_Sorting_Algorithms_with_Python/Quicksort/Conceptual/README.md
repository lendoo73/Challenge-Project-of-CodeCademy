#### [Cheatsheets](https://www.codecademy.com/learn/sorting-algorithms/modules/cs-quicksort/cheatsheet)

#### QUICKSORT: CONCEPTUAL

# [Introduction to Quicksort](https://www.codecademy.com/courses/sorting-algorithms/lessons/quicksort-conceptual/exercises/quicksort-conceptual-intro)

Quicksort is an efficient recursive algorithm for sorting arrays or lists of values. 
The algorithm is a comparison sort, where values are ordered by a comparison operation such as `>` or `<`.

Quicksort uses a *divide and conquer* strategy, breaking the problem into smaller sub-problems until the solution is so clear there’s nothing to solve.

The problem: many values in the array which are out of order.

The solution: break the array into sub-arrays containing at most one element. 
One element is sorted by default!

We choose a single pivot element from the list. 
Every other element is compared with the pivot, which partitions the array into three groups.
1. A sub-array of elements smaller than the pivot.
2. The pivot itself.
3. A sub-array of elements greater than the pivot.

The process is repeated on the sub-arrays until they contain zero or one element. 
Elements in the “smaller than” group are never compared with elements in the “greater than” group. 
If the smaller and greater groupings are roughly equal, this cuts the problem in half with each partition step!
```python
[6,5,2,1,9,3,8,7]
6 # The pivot
[5, 2, 1, 3] # lesser than 6
[9, 8, 7] # greater than 6
 
 
[5,2,1,3]  # these values
# will never be compared with 
[9,8,7] # these values
```
Depending on the implementation, the sub-arrays of one element each are recombined into a new array with sorted ordering, 
or values within the original array are swapped in-place, producing a sorted mutation of the original array.

[![Watch the video](https://img.youtube.com/vi/-oXfZUyA7Po/0.jpg)](https://youtu.be/-oXfZUyA7Po)



















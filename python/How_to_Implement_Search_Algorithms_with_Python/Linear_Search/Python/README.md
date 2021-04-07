#### LINEAR SEARCH: PYTHON

# [Introduction](https://www.codecademy.com/courses/search-algorithms/lessons/linear-implementation/exercises/intro-linear-implementation)

The linear search algorithm checks whether a value is an element in a list by scanning the elements of a list one-by-one.

The algorithm’s iterative approach to finding a target value is useful in solving numerous search problems with unsorted data.

# [Implement Linear Search](https://www.codecademy.com/courses/search-algorithms/lessons/linear-implementation/exercises/implement-linear-search)

Linear search is used to search for a target value in a list. 
We examine each of the elements in the list and compare them with the target value until matching the target.

If a match is found, the linear search function will return the index of the matching element. 
Otherwise, the function will raise a `ValueError`, a special error to indicate that the value was not found.

Here is the pseudocode for linear search as a function:
```
# For each element in the search_list
    # if element equal target value then
       # return its index
# if element is not found then 
    # raise a ValueError
```

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

# [Finding Duplicates](https://www.codecademy.com/courses/search-algorithms/lessons/linear-implementation/exercises/find-duplicates)

With a few changes to our code, we can modify linear search to solve more complex search problems.

Our linear search function, linear_search(), currently finds whether one given value exists in a list, returns the index of the first occurrence of the value in the list, and stops. But what if we wanted to find every occurrence of the target value in a list?

The following is a list of locations for your favorite music artist’s upcoming tour:

["New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]

In order to find all duplicates of a target value in a list, we modify the algorithm to match the following pseudocode:
```
# For each element in the searchList
  # if element equal target value then
    # Add its index to a list of occurrences
# if the list of occurrences is empty
  # raise ValueError
# otherwise
  # return the list occurrences
```

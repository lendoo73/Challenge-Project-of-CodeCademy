# `find_min()`
find the minimum value in a list.
```
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min
 
find_min([42, 17, 2, -1, 67])
# -1
find_mind([])
# None
find_min([13, 72, 19, 5, 86])
# 5
```
This solution has a linear runtime, or `O(N)`, where `N` is the number of elements in the list.

# [`is_palindrome()`](https://www.codecademy.com/courses/learn-recursion-python/lessons/iteration-recursion-python/exercises/iteration-recursion-python-palindrome)
Palindromes are words which read the same forward and backward. Here’s an iterative function that checks whether a given string is a palindrome:
```
def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True 
 
palindrome("abba")
# True
palindrome("abcba")
# True
palindrome("")
# True
palindrome("abcd")
# False
```
In each iteration of the loop that doesn’t return `False`, we make a copy of the string with two fewer characters.

Copying a list of `N` elements requires `N` amount of work in big O.

This implementation is a quadratic solution: we’re looping based on `N` and making a linear operation for each loop!

Here’s a more efficient version:
```
# Linear - O(N)
def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True
``` 
 

# [`multiplication()`](https://www.codecademy.com/courses/learn-recursion-python/lessons/iteration-recursion-python/exercises/iteration-recursion-python-multiplication)
Multiplication is repeated addition.
```
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result
 
multiplication(3, 7)
# 21
multiplication(5, 5)
# 25
multiplication(0, 4)
# 0
```
This implementation isn’t quite as robust as the built-in operator. It won’t work with negative numbers, for example.

#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [List Rotation: Slice](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-rotate-slice)

For our first problem, we would like to “rotate” a list, or **move elements forward** in a list by a number of spaces, `k`.

Elements at the greatest index will “wrap around” to the beginning of the list.
```Python
list = ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 0)
# ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 1)
# ['f', 'a', 'b', 'c', 'd', 'e']
rotate(list, 3)
# ['d', 'e', 'f', 'a', 'b', 'c']
```
## Clarifying Questions:

* Are there constraints on time or space efficiency? Nope! Just solve the problem.
* Should I account for negative inputs? The rotation input will always be positive.
* What if the rotation is greater than the list length? Continue wrapping! The “rotated” list would be the same as the original when `k` is equal to the length.

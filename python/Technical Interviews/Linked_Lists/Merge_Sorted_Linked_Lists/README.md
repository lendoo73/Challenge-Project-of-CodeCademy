#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LINKED LISTS

# [Merge Sorted Linked Lists](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-linked-lists/exercises/tip-python-ll-merge)

The next problem involves working with two different linked lists. 
You’ll need to write a function outside of the `LinkedList` class.

Given two sorted linked lists as input, your function should return a single sorted linked list made up of the nodes from both inputs.
```python
# linked_list_a = a -> c -> x -> z
# linked_list_b = b -> g -> u
 
merge(linked_list_a, linked_list_b)
# a -> b -> c -> g -> u -> x -> z
```
One way to solve this problem would be reassigning `.next` for each node in both lists. 
This approach is a constant space solution because we’re combining the inputs rather than creating a new linked list. 
In the above example, we would start by setting `'a'` node’s `.next` property to the `'b'` node.

Another way would be to create a new linked list. 
In the example, the head node of our new linked list would be `'a'` node.

## To recap:
* write a function: `merge()`.
* `merge()` takes two arguments: two sorted linked lists.
* return an instance of `LinkedList` which contains all the nodes from both of the input lists in sorted order.

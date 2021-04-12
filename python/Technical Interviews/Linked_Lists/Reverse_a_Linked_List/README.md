#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LINKED LISTS

# [Reverse a Linked List](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-linked-lists/exercises/tip-python-ll-reverse)

What if instead of progressing through nodes from head to tail, we wanted to move from tail to head? 
We can reverse a linked list to make this the default traversal!

Let’s examine what we’ll need to reverse the linked list.
```python
# a -> b -> c -> d
reverse(linked_list)
# d -> c -> b -> a
```
We reassign each node’s `.next` property to the preceding node. 
For the head node, this means `.next` points to `None`.

## To recap:
* write a function: `reverse()`.
* `reverse()` takes one argument, an instance of `LinkedList`.
* return an instance of `LinkedList` which contains all the nodes from the input in reverse order.

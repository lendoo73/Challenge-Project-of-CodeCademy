#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LINKED LISTS

# [Nth From Last](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-linked-lists/exercises/tip-python-ll-n-last)

Write a method which returns the node that is **`n` nodes from the tail of the linked list**.

If `n` is `0`, we would return the tail node, if `n` is `1`, we would return the second to last node, and so on.
```python
# a -> b -> c -> d -> e
linked_list.n_from_last(0)
# 'e' node
linked_list.n_from_last(3)
# 'b' node
```
We’ll need to be creative in how we solve this problem since we only have a reference to the head node and not the tail!

The `.size()` method on `LinkedList` may be helpful.

## To recap:
* write a method in the `LinkedList` class: `.n_from_last()`.
* `.n_from_last()` takes one argument:
  * the number of nodes counting from the tail.
* return the node instance at that location.

<details title="Click me to show...">
<summary>
 
## My solution

</summary>
<p>
     
```python
def n_from_last(self, n):
    size = self.size()
    current_node = self.head
    
    for i in range(size - n - 1):
        current_node = current_node.next
    
    return current_node
```

</p>
</details>

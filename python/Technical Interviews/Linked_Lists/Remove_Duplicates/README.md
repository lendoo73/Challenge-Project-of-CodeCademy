#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LINKED LISTS

# [Remove Duplicates](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-linked-lists/exercises/tip-python-ll-duplicates)

Our next problem **assumes a sorted linked list**. 
Nodes held at `.next` will have values greater than or equal to the current node’s value.

Write a method on the `LinkedList` class which removes all duplicates. 
In the following example, there are multiple nodes which hold the same value (`'a'` and `'c'`).
```python
# a -> a -> b -> c -> c -> c -> d
sorted_linked_list.remove_duplicates()
# a -> b -> c -> d
```
“Removing” nodes in a linked list is a matter of removing the reference to that node.
```python
# a -> b -> c
# a.next points to b
a.next = c
# a -> c
```
We have no way of reaching the node holding `'b'` once the `.next` property of the node holding `'a'` is set to the node holding `'c'`. 
We have “removed” `'b'` from the linked list. <a href="https://github.com/lendoo73/Challenge-Project-of-CodeCademy/blob/master/python/Linear_Data_Structures/Linked_Lists/Conceptual/README.md">(Orphaned node)</a>

## To recap:
* write a method in the `LinkedList` class: `.remove_duplicates()`.
* `.remove_duplicates()` takes no arguments.
* return `self` after all duplicate nodes are removed.

<hr />
<details title="Click me to show...">
<summary>
 
## My solution

</summary>
<p>
     
```python
def remove_duplicates(self):
    previous_node = self.head
    current_node = self.head.next
    
    # traverse to the end:
    while current_node:
        # check if the value is unique:
        value = current_node.val
        if value == previous_node.val:
            # this value is duplicated -> remove node:
            previous_node.next = current_node.next
        else:
            # unique value -> refresh the previous node
            previous_node = current_node
      
        # move to the next node:
        current_node = current_node.next
      
    return self
```

</p>
</details>
<hr />
<details title="Click me to show...">
<summary>
 
## CodeCademy solution

</summary>
<p>
     
```python

```

</p>
</details>

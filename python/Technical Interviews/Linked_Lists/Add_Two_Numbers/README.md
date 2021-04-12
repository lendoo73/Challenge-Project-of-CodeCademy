#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LINKED LISTS

# [Add Two Numbers](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-linked-lists/exercises/tip-python-ll-add)

For our last problem, we’re going to pretend that each node in a linked list holds the digit of a number. 
The **tail node** holds the *most significant digit* and the **head node** holds the *least significant digit*.
```python
# 2 -> 4 -> 1
# represents the number 142
# 7 -> 1
# represents the number 17
```
Given two of these linked lists, write a function that returns the sum of the two numbers as a new linked list.
```python
# 2 -> 4 -> 1
# plus
# 7 -> 1
# returns
# 9 -> 5 -> 1
```

## To recap:
* write a function: `add_two()`.
* `add_two()` takes two arguments, each an instance of `LinkedList`.
* return an instance of `LinkedList` which contains the sum of the input linked lists.

<hr />
<details title="Click me to show...">
<summary>
 
## My solution

</summary>
<p>
     
```python
def add_two(linked_list_a, linked_list_b):
    current_a = linked_list_a.head
    current_b = linked_list_b.head
    result_val = 0
    linked_list_result = LinkedList()
    tail = None

    while current_a or current_b:
        
        # add current values to the result value:
        if current_a:
            result_val += current_a.val
            current_a = current_a.next
        if current_b:
            result_val += current_b.val
            current_b = current_b.next
        
        # add current result value to the tail of linked list result:
        current_node_value = result_val % 10
        if not tail:
            linked_list_result.add(current_node_value)
            tail = linked_list_result.head
        else:
            tail.next = Node(current_node_value)
            tail = tail.next
        # reset result value with remainder:
        result_val = result_val // 10
  
    return linked_list_result
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
def add_two(linked_list_a, linked_list_b):
  
    result = LinkedList()
    carry = 0
  
    a_node = linked_list_a.head
    b_node = linked_list_b.head
  
    while a_node or b_node:
    
        if b_node:
            b_val = b_node.val
            b_node = b_node.next
        else:
            b_val = 0
      
        if a_node:
            a_val = a_node.val
            a_node = a_node.next
        else:
            a_val = 0
      
        to_sum = a_val + b_val + carry
    
        if to_sum > 9:
            carry = 1
            to_sum %= 10
        else:
            carry = 0

    
        if not result.head:
            result.head = Node(to_sum)
            tmp = result.head
        else:
            tmp.next = Node(to_sum)
            tmp = tmp.next
      
        if carry:
            tmp.next = Node(carry)

    return result
```

</p>
</details>


#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LINKED LISTS

# [Insert at Point](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-linked-lists/exercises/tip-python-ll-insert)
Write a method to insert a node anywhere in the linked list based on an input number. 
`0` means inserting at the head, `1` is the node following the head, and so on.
```python
# '->' is the .next property
# nodes are referenced by the values they hold
# x -> z means a node holding 'x'
# pointing to a node holding 'z'
 
# a -> b -> c -> d
linked_list.insert('x', 2)
# a -> b -> x -> c -> d
 
# 'b' node's next is set to x
# 'x' node's next is set to c
 
linked_list.insert('t', 0)
# t -> a -> b -> x -> c -> d
# head node is set to t
# 't' node's next is set to a
```
We’ll need to traverse from the head node and change the `.next` property on two nodes.

To recap:
* write a method in the `LinkedList` class: `.insert()`.
* `.insert()` takes two arguments:
  * the *value* which will be used to initialize a `Node`.
  * the insertion *location* for the node instance.
* return `self` at the end of the function.


<details>
<summary style="font-size: 20px;"> **My solution** </summary>
<p>
     
```python
def insert(self, node_value, location):
    # if location is 0 insert to the head
    if location == 0:
        self.add(node_value)
        return self
    
    # location greater than 0; traverse to location:
    current_node = self.head
    for i in range(1, location):
        if current_node.next:
            current_node = current_node.next
        else: 
            print("Run out from index")
            return self
            
    # location found -> insert new node:
    # look for tail:
    if not current_node.next:
        # we are at tail:
        new_node = Node(node_value)
    else:
        # we are at middle:  
        new_node = Node(node_value, current_node.next)
    current_node.next = new_node
    return self
```

</p>
</details>

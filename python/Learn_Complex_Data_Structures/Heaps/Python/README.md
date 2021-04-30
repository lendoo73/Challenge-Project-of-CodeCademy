#### HEAPS: PYTHON

# [Min-Heaps of Fun](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-intro)

We’re going to implement a min-heap in Python. 
**Min-heaps** efficiently **keep track of the minimum value in a dataset**, even as we add and remove elements.

Min-heaps are nearly identical to a max-heap, just with the comparisons reversed. 
It’s a two for one lesson!

Heaps enable solutions for complex problems such as finding the shortest path (Dijkstra’s Algorithm) or efficiently sorting a dataset (heapsort).

They’re an essential tool for confidently navigating some of the difficult questions posed in a technical interview.

By understanding the operations of a heap, you will have made a valuable addition to your problem-solving toolkit.

# [Defining Min-Heap](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-heap)

Our MinHeap class will store two pieces of information:
* A Python list of the elements within the heap.
* A count of the elements within the heap.

To make our lives easier, we’ll always keep one *sentinel* element at the beginning inside the list: `None`.
```py
heap = MinHeap()
print(heap.heap_list)
# [None]
print(heap.count)
# 0
```
This dummy value will save us the trouble of checking whether the list is empty and simplify the methods we define in later lessons.
```py
class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0
```

# [Adding an Element: Heapify Up I](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-heapify-up-i)

The min-heap is no good if all it ever contains is `None`. 
Let’s build the functionality to add elements while maintaining the heap properties.

Our `MinHeap` will abide by two principles:
* The element at **index `1`** is the **minimum value** in the entire list.
* Every **“child”** element in the list must be **larger than** their **“parent”**.

The first element we add to the list will be the minimum because there are no other elements. 

For now, let’s define `.add()` which will allow us to add elements into the `.heap_list`. 
We’ll also start defining `.heapify_up()`, which will do the work of maintaining the heap properties as we add additional elements.
```py
  def add(self, element):
    print("Adding element to self.heap_list.")
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()
```
```py
  def heapify_up(self):
    print("Restoring the heap property…")
```

# [Translating Parent and Child Elements Into Indices](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-indices)

Our `MinHeap` adds elements to the internal list, keeps a running count, and has the beginnings of `.heapify_up()`.

Before we dive into the logic for `.heapify_up()`, let’s review how heaps track elements. 
We use a list for storing internal elements, but we’re modeling it on a binary tree, where every “parent” element has up to two “child” elements.

“child” and “parent” elements are determined by their relative indices within the internal list. 
By doing some arithmetic on an element’s index, we can determine the indices for parent and child elements (if they exist).
* **Parent**: `index // 2`
* **Left Child**: `index * 2`
* **Right Child**: `(index * 2) + 1`
```py
print(heap.heap_list)
#        [None, 10, 13, 21, 61, 22, 23, 99]
# Indices: [0, 1, 2, 3, 4, 5, 6, 7]
 
heap.parent_idx(4)
# (4 // 2) == 2
# Element at index 4 is 61 
# Element at index 2 is 13
# The parent element of 61 is 13
 
heap.left_child(3)
# (3 * 2) == 6
# Element at index 3 is 21
# Element at index 6 is 23
# The left child element of 21 is 23
```
These calculations are important for the efficiency of the heap, but they’re not necessary to memorize, so we’ve added three helper methods: 
* `.parent_idx()`, 
* `.left_child_idx()`, 
* and `.right_child_idx()`.

These helpers take an index as the argument and return the corresponding parent or child index.
```py
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1
```

# [Adding an Element: Heapify Up II](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-heapify-up-ii)

Now that we understand how to determine the relationship of elements with the internal list, we’re ready to finish `.heapify_up()`.

We need to make sure that every child is greater in value than their parent. 
Say we add an element to the following heap:
```py
print(heap.heap_list)
# [None, 10, 13, 21, 61, 22, 23, 99]
heap.add(12)
 
# ( new_element )
# { parent_element }
# [None, 10, 13, 21, {61}, 22, 23, 99, (12)]
```
Oh no! 
We’ve violated the heap property: `12`‘s parent is `61`, the parent element is greater than the child.

Don’t fret; we can fix this. 
We’ll exchange the parent and the child elements.
```py
# [None, 10, 13, 21, {61}, 22, 23, 99, (12)]
# SWAP 12 and 61
# [None, 10, 13, 21, (12), 22, 23, 99, {61}]
```
`12`‘s parent is now `13`, they’re close but the parent element is still greater than the child. Keep on swappin’!
```py
# [None, 10, {13}, 21, (12), 22, 23, 99, 61]
# SWAP 12 and 13
# [None, 10, (12), 21, {13}, 22, 23, 99, 61]
```
Okay, you can let out that sigh of relief. 
We’ve restored the heap properties!
```py
# [None, {10}, (12), 21, 13, 22, 23, 99, 61]
# The child, 12, is greater than the parent, 10!
```
Let’s recap our strategy for `.heapify_up()`:
```py
# start at the last element of the list
# while there's a parent element available:
  # if the parent element is greater:
    # swap the elements
  # set the target element index to be the parent's index
```
```py
  def heapify_up(self):
    print("Heapifying up")
    # start at the last element of the list
    idx = self.count
    # while there's a parent element available:
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      
      # if the parent element is greater:
      if parent > child:
        print(f"swapping {parent} with {child}")
        # swap the elements
        self.heap_list[self.parent_idx(idx)], self.heap_list[idx] = self.heap_list[idx], self.heap_list[self.parent_idx(idx)]
      
      # set the target element index to be the parent's index
      idx = self.parent_idx(idx)
    
    print(f"Heap Restored {self.heap_list}")
```

# [Removing the Min](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-retrieve-min)

Min-heaps would be useless if we couldn’t retrieve the minimum value. 
We’ve gone through a lot of work to maintain that value because we’re going to need it!

Our goal is **to efficiently remove the minimum element** from the heap. 
You’ll recall that we always locate the minimum element at index `1`, (a sentinel element occupies index `0`).

Our internal list mirrors a binary tree. 
There’s a delicate balance of parent and child relationships we would ruin by directly removing the minimum.
```py
print(heap.heap_list)
# [None, 10, 21, 13, 61, 22, 23, 99]
heap.retrieve_min()
# 10
# [None, ???, 21, 13, 61, 22, 23, 99]
```
We need to remove an element that has no children; we need to remove the last element. 
Swap the minimum with the last element, and we can easily remove the minimum from the end of the list.
```py
# [None, (10), 21, 13, 61, 22, 23, {99}]
heap.retrieve_min()
# [None, {99}, 21, 13, 61, 22, 23, (10)]
# [None, 99, 21, 13, 61, 22, 23]
# 10
```
Terrific! We removed the minimum element with minimal disruption. 
Unfortunately, our heap is out of shape again with `99` sitting where the minimum element should be.

We will solve this in lessons to come…
```py
  def retrieve_min(self):
    if not self.count: 
      return print("No items in heap")

    min = self.heap_list[1]
    print(f"Removing: {min} from {self.heap_list}")
    # swap first element with the last one
    self.heap_list[1], self.heap_list[self.count] = self.heap_list[self.count], self.heap_list[1]
    # remove the last (min) element
    self.heap_list.pop()
    # decrement the counter
    self.count -= 1
    print(f"Last element moved to first: {self.heap_list}")
    return min
```

# [Heapify Down I](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-heapify-down-i)

We’ve retrieved the minimum element but left our `MinHeap` in disarray. 
There’s no reason to get discouraged, we’ve handled this type of problem before, and we can get our `MinHeap` back in shape!

We’ll define a method, `.heapify_down()`, which performs a similar role to `.heapify_up()`, except now we’re moving down the “tree” instead of up.
```py
  def heapify_down(self):
    print("Heapifying down!")
    idx = 1
```

# [Finding the Smallest Child](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-smallest-child)

We mentioned `.heapify_down()` is a lot like `.heapify_up()`. 
We’ll track an offending element in the heap, and keep swapping it with another element until we’ve restored the heap properties.

The wrinkle is `.heapify_down()` gives us another option for which element to swap. 
In `.heapify_up()`, we were always comparing our element with its parent. 
In `.heapify_down()`, we have potentially two options: the left child and the right child.

Which should we choose? 
We’ll use an example to think it through. 
Imagine we have a heap with four elements:
```py
print(heap.heap_list)
# [None, 21, 36, 58, 42]
heap.retrieve_min()
# 21
# [None, 42, 36, 58]
# Should we swap with 36 or 58?
```
We want to swap with the smaller of the two children, otherwise, we wouldn’t maintain our heap properties!

Let’s write a helper method to determine the smallest child element for a given index. 
We’ll make heavy use of our other helper methods: `.left_child_idx()` and `.right_child_idx()`.

`.get_smaller_child_idx()` will have the following structure:
```py
# check if we have a right child
  # if we don't, return the left child index
  # if we do...
    # return the index of the smaller child
```
```py
  def get_smaller_child_idx(self, idx):
    right_child_idx = self.right_child_idx(idx)
    left_child_idx = self.left_child_idx(idx)
    if right_child_idx > self.count:
      # we don't have right child
      print("There is only a left child")
      return left_child_idx
    
    # we have right child too, compare which is smaller
    left_child = self.heap_list[self.left_child_idx(idx)]
    right_child = self.heap_list[self.right_child_idx(idx)]

    if left_child < right_child:
      print("Left child ({left_child}) is smaller.")
      return left_child_idx
    else:
      print("Right child ({right_child}) is smaller or equal.")
      return right_child_idx

```

# [Removing the Min: Heapify Down II](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-heapify-down-ii)

We’ve got a handy helper to tell us which child element is smaller, so there’s nothing standing between us and a pristine heap.

As a reminder, our strategy will be very similar to `.heapify_up()`, but we’ll be moving down the tree. 
Here’s the general shape of the method:
```py
 # starting with our first element...
 # while there's at least one child present:
   # get the smallest child's index
   # compare the smallest child with our element
     # if our element is larger, swap with child
   # regardless, set our element index to be the child
```
We’ve added another helper method for you: `.child_present()`. 
This returns a boolean indicating whether a given index has an associated child element.
```py
  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count
```
```py
  def heapify_down(self):
    idx = 1

    while self.child_present(idx):
      print("Heapifying down!")
      smaller_child_idx = self.get_smaller_child_idx(idx)
      
      child = self.heap_list[smaller_child_idx]
      parent = self.heap_list[idx]

      if parent > child:
        # swap parent with child:
        self.heap_list[idx] = child
        self.heap_list[smaller_child_idx] = parent

      idx = smaller_child_idx

    print(f"Heap Restored! {self.heap_list}")
```

# [Min-Heap Review](https://www.codecademy.com/courses/complex-data-structures/lessons/python-heaps/exercises/python-heaps-review)

You’ve implemented a min-heap in Python, and that’s no small feat (although it could efficiently track the smallest feat).

To recap: `MinHeap` tracks the minimum element as the element at index `1` within an internal Python list.

When adding elements, we use `.heapify_up()` to compare the new element with its parent, making swaps if it violates the heap property: 
**children must be greater than their parents.**

When removing the minimum element, we swap it with the last element in the list. 
Then we use `.heapify_down()` to compare the new root with its children, swapping with the smaller child if necessary.

Heaps are so useful because they’re efficient in maintaining their heap properties. 
Building a heap using elements that decreased in value would ensure that we continually violated the heap property. 
How many swaps would that cause?

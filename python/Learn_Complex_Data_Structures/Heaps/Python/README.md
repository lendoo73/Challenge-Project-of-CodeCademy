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














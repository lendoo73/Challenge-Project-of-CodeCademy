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


















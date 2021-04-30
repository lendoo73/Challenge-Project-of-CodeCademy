# import heap class
from min_heap import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# set internal list for testing purposes...
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
min_heap.count = 7

while len(min_heap.heap_list) != 1:
  print(min_heap.heap_list)
  min_heap.retrieve_min()

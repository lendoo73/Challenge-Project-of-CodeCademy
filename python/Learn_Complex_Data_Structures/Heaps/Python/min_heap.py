class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # NEW HELPER!
  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS
  
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    min = self.heap_list[1]
    print("Removing: {0} from {1}".format(min, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))    
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
      
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


  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        print("Left child is smaller")
        return self.left_child_idx(idx)
      else:
        print("Right child is smaller")
        return self.right_child_idx(idx)
    
  def heapify_up(self):
    idx = self.count
    while self.parent_idx(idx) > 0:
      if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        tmp = self.heap_list[self.parent_idx(idx)]
        print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
        self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = self.parent_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("")
    

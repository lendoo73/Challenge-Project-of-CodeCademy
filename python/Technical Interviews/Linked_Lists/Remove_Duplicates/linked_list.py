from node import Node

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

  def add(self, val):
    new_head = Node(val)
    new_head.next = self.head
    self.head = new_head
    
  def remove_duplicates(self):
    previous_node = self.head
    current_node = self.head.next
    
    # traverse to the end:
    while current_node:
      # check if the value is unique:
      value = current_node.val
      if value == previous_node.val:
        # this value is duplicated; remove node:
        previous_node.next = current_node.next
      else:
        # unique value; refresh the previous node
        previous_node = current_node
      
      # move to the next node:
      current_node = current_node.next
      
    return self
    
  def traverse(self):
    head = self.head
    print("Starting traversal from head")
    while head:
      print("visiting node: {0}".format(head.val))
      head = head.next
    print("Traversal complete")
    
  def size(self):
    node_count = 0
    current_node = self.head
    while current_node:
      node_count += 1
      current_node = current_node.next
    return node_count
  
  def __repr__(self):
    text = ''
    head = self.head
    while head:
      text += str(head.val) + ' -> '
      head = head.next
    return text

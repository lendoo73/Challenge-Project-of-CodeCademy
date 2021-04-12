from node import Node

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node
    
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
    

  def add(self, val):
    new_head = Node(val)
    new_head.next = self.head
    self.head = new_head
    
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

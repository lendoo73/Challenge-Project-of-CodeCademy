from node import Node

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

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
    repeat = {}
    while head:
      if repeat.get(id(head), False):
        text += str(head.val) + ' -> '
        text += "\nCYCLE DETECTED, stopping traversal..."
        break
      else:
        repeat[id(head)] = True
        text += str(head.val) + ' -> '
        head = head.next
    return text
  
def build_cycle_linked_list():
  start_node = Node('a')
  head = start_node
  b = Node('b')
  c = Node('c')
  d = Node('d')
  for letter_node in [b, c, d]:
    start_node.next = letter_node
    start_node = start_node.next
  start_node.next = b
  return LinkedList(head)
  
def build_linked_list_no_cycle():
  start_node = Node('a')
  head = start_node
  
  for letter in ['b', 'c', 'd', 'b']:
    start_node.next = Node(letter)
    start_node = start_node.next
  return LinkedList(head)
  

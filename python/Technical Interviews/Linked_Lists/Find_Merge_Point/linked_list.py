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
    while head:
      text += str(head.val) + ' -> '
      head = head.next
    return text
  
  
def set_up_test_case():
  head_node_1 = Node('x')
  head_node_2 = Node('d')
  current_node_1 = head_node_1
  current_node_2 = head_node_2
  
  for letter in ['a', 'b']:
    current_node_1.next = Node(letter)
    current_node_1 = current_node_1.next
    
  current_node_2.next = Node('f')
  current_node_2 = current_node_2.next
  
  for shared_node in [Node('q'), Node('e')]:
  	current_node_1.next = shared_node
  	current_node_2.next = shared_node
  	current_node_1 = current_node_1.next
  	current_node_2 = current_node_2.next
    
  linked_list_1 = LinkedList(head_node_1)
  linked_list_2 = LinkedList(head_node_2)
  return linked_list_1, linked_list_2

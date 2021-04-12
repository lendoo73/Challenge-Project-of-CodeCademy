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
  
def build_test_case():
  linked_list_a = LinkedList()
  linked_list_a.add(1)
  linked_list_a.add(4)
  linked_list_a.add(2)
  linked_list_b = LinkedList()
  linked_list_b.add(1)
  linked_list_b.add(7)
  return linked_list_a, linked_list_b

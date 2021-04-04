class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value = None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove, remove_all = False):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
      if remove_all == False:
        return
      else:
        self.remove_node(value_to_remove, True)
    while current_node:
      next_node = current_node.get_next_node()
      if next_node.get_value() == value_to_remove:
        current_node.set_next_node(next_node.get_next_node())
        if remove_all == False:
          break
      if next_node.get_next_node():
        current_node = next_node
      else: break
        
  def remove_all_node(self, value_to_remove):
    self.remove_node(value_to_remove, True)

my_list = LinkedList(1)
my_list.insert_beginning(1)
my_list.insert_beginning(2)
my_list.insert_beginning(3)
my_list.insert_beginning(1)
print("my_list:\n",my_list.stringify_list())
my_list.remove_node(3)
print("Remove '3' from my_list:\n", my_list.stringify_list())
my_list.remove_all_node(1)
print("remove all '1' from my_list:\n", my_list.stringify_list())

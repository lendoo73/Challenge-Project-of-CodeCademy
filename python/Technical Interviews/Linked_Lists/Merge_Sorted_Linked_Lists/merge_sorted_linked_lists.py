from linked_list import LinkedList, Node

linked_list_a = LinkedList()
linked_list_b = LinkedList()
linked_list_a.add('z')
linked_list_a.add('x')
linked_list_a.add('c')
linked_list_a.add('a')
linked_list_b.add('u')
linked_list_b.add('g')
linked_list_b.add('b')


def merge(linked_list_a, linked_list_b):
  current_a_node = linked_list_a.head
  current_b_node = linked_list_b.head
  if current_a_node.val > current_b_node.val:
    # swap to start with the smaller header:
    current_a_node, current_b_node = current_b_node, current_a_node
  
  while current_b_node:
    if current_a_node.next.val < current_b_node.val:
      # got to next a:
      current_a_node = current_a_node.next
    else:
      # cut both list:
      temporary_a = current_a_node.next 
      temporary_b = current_b_node.next 

      # insert 'current b':
      current_a_node.next = current_b_node
      # merge the cutted lists:
      current_a_node.next.next = temporary_a
      current_b_node = temporary_b 
  
  return linked_list_a

  

merged_linked_list = merge(linked_list_a, linked_list_b)

print("Merged list should contain all nodes in sorted order: a -> b -> c -> g -> u -> x -> z")
print("Your function returned: {0}".format(merged_linked_list))

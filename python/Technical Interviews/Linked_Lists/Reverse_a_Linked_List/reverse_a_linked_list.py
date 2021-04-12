from linked_list import LinkedList, Node

test_linked_list = LinkedList()

test_linked_list.add('d')
test_linked_list.add('c')
test_linked_list.add('b')
test_linked_list.add('a')


def reverse(linked_list):
  print(linked_list)
  prev_node = linked_list.head
  current_node = linked_list.head.next

  while current_node:
    # add current node to the beginning:
    linked_list.add(current_node.val)
    # delete current node:
    prev_node.next = current_node.next

    current_node = current_node.next
    
  return linked_list


print("Pre-reverse: {0}".format(test_linked_list))

reversed_linked_list = reverse(test_linked_list)

print("Post-reverse: {0}".format(reversed_linked_list))

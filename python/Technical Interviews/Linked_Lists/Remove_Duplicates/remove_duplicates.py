from linked_list import LinkedList, Node

test_linked_list = LinkedList()

test_linked_list.add('d')
test_linked_list.add('c')
test_linked_list.add('c')
test_linked_list.add('c')
test_linked_list.add('b')
test_linked_list.add('a')
test_linked_list.add('a')

print(test_linked_list)
test_linked_list.remove_duplicates()
print(test_linked_list)
duplicates = {}
duplicate_found = False
current_node = test_linked_list.head
while current_node:
  if duplicates.get(current_node.val, False):
    duplicate_found = True
    break
  else:
    duplicates[current_node.val] = True
    current_node = current_node.next

if duplicate_found:
  print("Not all duplicates removed, try again!")
else:
  print("Duplicates removed, nice work!")

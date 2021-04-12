from linked_list import LinkedList, Node, build_cycle_linked_list, build_linked_list_no_cycle


cycle_linked_list = build_cycle_linked_list()
no_cycle_linked_list = build_linked_list_no_cycle()

def has_cycle(linked_list):
  current_node = linked_list.head
  unique = []
  
  while current_node:
    node_id = id(current_node)
    if node_id in unique:
      return True
    else:
      unique.append(node_id)
    current_node = current_node.next

  return False

cycle_result = has_cycle(cycle_linked_list)
no_cycle_result = has_cycle(no_cycle_linked_list)

print("Should return True when a cycle exists: {0}".format(cycle_result))

print("Should return False when a cycle does not exist: {0}".format(no_cycle_result))


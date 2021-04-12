from linked_list import LinkedList, Node, build_test_case

linked_list_a, linked_list_b = build_test_case()

def add_two(linked_list_a, linked_list_b):
  current_a = linked_list_a.head
  current_b = linked_list_b.head
  result_val = 0
  linked_list_result = LinkedList()
  tail = None

  while current_a or current_b:
    # add current values to the result value:
    if current_a:
      result_val += current_a.val
      current_a = current_a.next
    if current_b:
      result_val += current_b.val
      current_b = current_b.next
    # add current result value to the tail of linked list result:
    current_node_value = result_val % 10
    if not tail:
      linked_list_result.add(current_node_value)
      tail = linked_list_result.head
    else:
      tail.next = Node(current_node_value)
      tail = tail.next
    # reset result value with remainder:
    result_val = result_val // 10
    print(linked_list_result)

  
  return linked_list_result


print("Adding linked list:\n{0}\nto linked list\n{1}\n".format(linked_list_a, linked_list_b))
result = add_two(linked_list_a, linked_list_b)
print("Result should be: 9 -> 5 -> 1 ->\nFunction returned:\n{0}".format(result))

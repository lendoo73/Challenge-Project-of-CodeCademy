from linked_list import LinkedList, Node, set_up_test_case

linked_list_1, linked_list_2 = set_up_test_case()

def merge_point(linked_list_a, linked_list_b):
  current_a = linked_list_a.head
  current_b = linked_list_b.head
  unique = []
  
  while current_a or current_b:
    
    if current_a:
      # insert id to the unique list
      id_a = id(current_a)
      # check merge point:
      if id_a in unique:
        return current_a
      else: unique.append(id_a)

      # move to the next node:
      current_a = current_a.next
    
    if current_b:
      id_b = id(current_b)
      if id_b in unique:
        return current_b
      else: unique.append(id_b)
      current_b = current_b.next

  return None

test_result = merge_point(linked_list_1, linked_list_2)

print("Function should return merge point node holding 'q': {0}".format(test_result.val))

def merge(linked_list_a, linked_list_b):
  
  current_node_a = linked_list_a.head
  current_node_b = linked_list_b.head
  
  if current_node_a.val < current_node_b.val:
    start_node = current_node_a
    current_node_a = current_node_a.next
  else:
    start_node = current_node_b
    current_node_b = current_node_b.next

  head = start_node
  
  while current_node_a or current_node_b:
    if not current_node_a:
      start_node.next = current_node_b
      current_node_b = current_node_b.next
    elif not current_node_b:
      start_node.next = current_node_a
      current_node_a = current_node_a.next
    elif current_node_a.val < current_node_b.val:
      start_node.next = current_node_a
      current_node_a = current_node_a.next
    else:
      start_node.next = current_node_b
      current_node_b = current_node_b.next
    start_node = start_node.next
    
  return LinkedList(head)

def merge_point(linked_list_a, linked_list_b):
  size_of_a = linked_list_a.size()
  size_of_b = linked_list_b.size()
  
  diff = abs(size_of_a - size_of_b)
    
  if size_of_a > size_of_b:
    bigger = linked_list_a.head
    smaller = linked_list_b.head
  else:
    bigger = linked_list_b.head
    smaller = linked_list_a.head
  
  for i in range(diff):
    bigger = bigger.next

  while bigger and smaller:
    if bigger == smaller:
      return bigger
    bigger = bigger.next
    smaller = smaller.next

  return None

def reverse(linked_list):
    prev = None
    current_node = linked_list.head
    while current_node:
      tmp = current_node.next
      current_node.next = prev
      prev = current_node
      current_node = tmp
    return LinkedList(prev)

def has_cycle(linked_list):
  slow, fast = linked_list.head, linked_list.head
  while slow and fast:
    slow = slow.next
    fast = fast.next
    if fast:
      fast = fast.next
    else:
      return False
    if fast == slow:
      return True
  return False

def add_two(linked_list_a, linked_list_b):
  
  result = LinkedList()
  carry = 0
  
  a_node = linked_list_a.head
  b_node = linked_list_b.head
  
  while a_node or b_node:
    
    if b_node:
      b_val = b_node.val
      b_node = b_node.next
    else:
      b_val = 0
      
    if a_node:
      a_val = a_node.val
      a_node = a_node.next
    else:
      a_val = 0
      
    to_sum = a_val + b_val + carry
    
    if to_sum > 9:
      carry = 1
      to_sum %= 10
    else:
      carry = 0

    
    if not result.head:
      result.head = Node(to_sum)
      tmp = result.head
    else:
      tmp.next = Node(to_sum)
      tmp = tmp.next
      
  if carry:
    tmp.next = Node(carry)

  return result

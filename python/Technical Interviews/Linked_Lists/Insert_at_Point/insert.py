from linked_list import LinkedList

test_1 = LinkedList()
test_1.add('d')
test_1.add('c')
test_1.add('b')
test_1.add('a')
test_1.insert('x', 2)

test_result = test_1.head
for i in range(2):
  test_result = test_result.next
print("Result node's value should be 'x': {0}".format(test_result.val))

test_1.insert('t', 0)
test_result = test_1.head
print("Result node's value should be 't': {0}".format(test_result.val))

print(test_1)

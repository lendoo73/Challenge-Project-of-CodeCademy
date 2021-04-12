from linked_list import LinkedList, Node

test_list = LinkedList()
test_list.add('e')
test_list.add('d')
test_list.add('c')
test_list.add('b')
test_list.add('a')
print(test_list)
test_result = test_list.n_from_last(0)

print("Result node's value should be 'e': {0}".format(test_result.val))

test_result = test_list.n_from_last(3)
print("Result node's value should be 'b': {0}".format(test_result.val))

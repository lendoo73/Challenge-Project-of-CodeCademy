from linked_list import LinkedList, Node

# initializing linked list with NO head node to start
linked_list_1 = LinkedList()
linked_list_1.add('hey!')
linked_list_1.add('ho!')
linked_list_1.add("let's go!")
linked_list_1.traverse()
# The last added node is the head using .add()!

# We can also add nodes without .add()!
# assigning a Node's .next property directly...
lyric_node_1 = Node('cool')
lyric_node_2 = Node('beans!')
lyric_node_1.next = lyric_node_2

# initializing a linked list WITH a head node
linked_list_2 = LinkedList(lyric_node_1)
print(linked_list_2)

# We can also build up a linked list with a loop!
current_node = Node("Let's count to 5!")
# save a reference to the head to pass to LinkedList
head = current_node 
for i in range(1, 6):
  current_node.next = Node(i) 
  current_node = current_node.next

linked_list_3 = LinkedList(head) # passing head as argument
print(linked_list_3)
print("This linked list has {0} nodes!".format(linked_list_3.size()))

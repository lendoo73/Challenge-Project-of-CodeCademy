# Adding in the Linked List
# 12. Import the linked list and node library
from linked_list import Node, LinkedList
# Adding the Flower Definitions
# 22. import the flower definitions
from blossom_lib import flower_definitions 

# Building Out The Hash Map
# 1. define our HashMap class
class HashMap:
  # 2. constructor
  def __init__(self, size):
    self.array_size = size
    #self.array = [None] * size
    # 13. Change array of None to Linkedlist
    self.array = [LinkedList()] * size
  
  # internal methods:
  # 3 - 4.
  def hash(self, key):
    return sum(key.encode())
  
  # 5.
  def compressor(self, hash_code):
    return hash_code % self.array_size

  # external methods:
  # 6.
  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compressor(hash_code)
    # 7.
    #self.array[array_index] = [key, value]
    # Adding in Separate Chaining: Assignment
    # 14. Create a new Node object
    payload = Node([key, value])
    # 15. We’ll need to check if the key exists in the LinkedList
    list_at_array = self.array[array_index]
    # 16. Iterate through `list_at_array`
    for item in list_at_array:
      if item[0] == key:
        # 17. overwrite 
        item[1] = value
        return 
    # 18. we’ve iterated through the list and not found our key
    list_at_array.insert(payload)

  # 8 - 9.
  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compressor(hash_code)
    # 10. Save the value
    #payload = self.array[array_index]
    # Adding in Separate Chaining: Retrieval
    # 19.
    list_at_index = self.array[array_index]
    # 20. Iterate through the linked list 
    for item in list_at_index:
      if item[0] == key:
        # 21. we find the key, return the value
        return item[1]
    # 11.
    #if payload is None or payload[0] != key:
      #return None
    return None
    
    return payload[1]

# 23. create a new instance of our HashMap
blossom = HashMap(len(flower_definitions))

# 24. for every element of flower_definitions, assign the value to its key
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

# 25. Now use our app
print(blossom.retrieve('daisy'))

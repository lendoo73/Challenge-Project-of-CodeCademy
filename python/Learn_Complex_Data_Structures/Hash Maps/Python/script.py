class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions = 0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def get_array_value(self, key, count_collisions = 0):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]

  def assign(self, key, value, delete = False):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None or current_array_value[0] == key:
      if delete:
        self.array[array_index] = None
      else:
        self.array[array_index] = [key, value]
      return

    # Collision!
    number_collisions = 1

    while(current_array_value[0] != key):
      current_array_value = self.get_array_value(key, number_collisions)

      if current_array_value is None:
        if delete:
          self.array[array_index] = None
        else:
          self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    possible_return_value = self.get_array_value(key)

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      possible_return_value = self.get_array_value(key, retrieval_collisions)

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return
  
  def delete(self, key):
    self.assign(key, "", True)

hash_map = HashMap(15)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")

print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))

hash_map.delete("gneiss")

print(hash_map.retrieve("béla"))
print(hash_map.retrieve("gneiss"))
hash_map.delete("béla")

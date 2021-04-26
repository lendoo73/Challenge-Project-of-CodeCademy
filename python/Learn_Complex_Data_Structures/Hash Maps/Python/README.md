#### HASH MAPS: PYTHON

# [Creating the Hash Map Class](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/creating-the-class)

Hash maps are efficient key-value stores. 
They are capable of assigning and retrieving data in the fastest way possible for a data structure. 
This is because the underlying data structure that they use is an array. 
A value is stored at an array index determined by plugging the key into a hash function.

In Python we don’t have an array data structure that uses a contiguous block of memory. 
We are going to simulate an array by creating a list and keeping track of the size of the list with an additional integer variable. 
This will allow us to design something that resembles a hash map. 
This is somewhat elaborate for the actual storage of a key-value pair, 
but it helps to remember that the purpose of this lesson is to gain a deeper understanding of the structure as it is constructed. 
For real-world use cases in which a key-value store is needed, **Python** offers a built-in hash table implementation with **dictionaries**.

```python
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size 
    self.array = [None] * array_size
  
my_map = HashMap(5)
print(my_map.array)
```

# [Creating the Hashing Function](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/creating-the-hash-function)

The necessary ingredient in the hash map recipe is the hashing function. 
A hashing function takes a key and returns an index into the underlying array.

Hash functions need to be fast to compute so that access and retrieval can be done fast.
```python
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code
```

# [Creating the Compression Function](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/creating-the-compression-function)

Hashing functions return a wide range of integers. 
In order to transform these values into useful indices for our array we need a compression function. 
A compression function uses modular arithmetic to calculate an array index for a hash map when given a hash code.
```python
  def compressor(self, hash_code):
    return hash_code % self.array_size
```

# [Defining the Setter](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/defining-the-setter)

We need to put together all the other steps we’ve taken: 
* plug the key into the hash function, 
* plug the hash code into the compression function, 
* use the array index to find the place in the array, 
* and finally set the value of the array to the value we want.

```python
  def assign(self, key, value):
    hash_code = self.hash(key)                 # plug the key into the hash function
    index = self.compressor(hash_code)         # plug the hash code into the compression function
    self.array[index] = value                  # use the array index to find the place in the array
```
The next step is to set the value of the array to the value we want.

# [Defining the Getter](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/defining-the-getter)

There is a natural expectation after placing an item into a bag that we will later be able to remove the item from that bag. 
Otherwise we have created a hole. 
Let’s implement retrieval for our hash map.
```python
  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compressor(hash_code)
    return self.array[array_index]
```

# [Creating an Instance](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/creating-an-instance)

Since we have the basic functionality of a hash map, let’s create a test instance of one for us to make sure everything works as expected.
```python
hash_map = HashMap(20)
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gneiss"))           # Output: metamorphic
```

# [Handling Collisions in the Setter](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/handling-collisions-setter)

Our hash and compression functions together can result in collisions. 
This is when two different keys resolve to the same array index. 
In our current implementation, all keys that resolve to the same index are treated as if they are the same key.

Our first step in implementing a collision strategy is updating our `.assign()` and `.retrieve()` methods to set the value with the key 
and check the key before retrieving a value.
```python
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    
    if current_array_value == None:
      self.array[array_index] = [key, value]
    elif current_array_value[0] == key:
      self.array[array_index][1] = value
```

# [Handling Collisions in the Getter](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/handling-collisions-getter)

When we retrieve hash map values, we also need to be aware of the fact that two keys could point to the same array index.
```python
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]
    if possible_return_value is None:
      return None  
    elif possible_return_value[0] == key:
      return possible_return_value[1]
```

# [Open Addressing](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/open-addressing)

Now we’re going to implement an open addressing system so our hash map can resolve collisions. 
In open addressing systems, we check the array at the address given by our hashing function. 
One of three things can happen:
* The address points to an **empty** cell.
* The cell **holds a value for the key** we are getting/setting
* The cell **holds a value for a different key**.

In the first case, this means that the hash map does not have a value for the key and no collision resolution needs to happen. 
Notice that this does not work if we want to be able to delete keys in our hash map. 
There are strategies for deleting pairs from a hash map (see [Lazy Deletion](https://en.wikipedia.org/wiki/Lazy_deletion)) but we will not be investigating these.

In the second case, we’ve found the value for our key-value pair!

In the third case, we need to use our collision addressing strategy to find if our key is somewhere else (it may or may not be) 
so we should recalculate the index of our array.

We give the `hash()` method another parameter: `count_collisions`. 
This will be the number of times the `.hash()` has hit a collision.
```python
  def hash(self, key, count_collisions = 0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions
```

# [Open Addressing in the Setter](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/open-addressing-setter)

Now lets use our open addressing scheme in the setter for our `HashMap`.
```python
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # current_array_value currently holds different key
    number_collisions = 1
    while current_array_value[0] != key:
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return
      if current_array_value[0] == key:
        self.array[new_array_index][1] = value
      return
      number_collisions +=1
    
    return

```

# [Open Addressing in the Getter](https://www.codecademy.com/courses/complex-data-structures/lessons/hash-maps-implementation/exercises/open-addressing-getter)

With everything in our setter taken care of, we want to make sure that when we retrieve our value we’re retrieving the correct value.
```python
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    retrieval_collisions = 1
    while possible_return_value[0] != key:
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]
      if possible_return_value is None:
        return None
      if possible_return_value[0] != key:
        retrieval_collisions += 1
      if possible_return_value[0] == key:
        return possible_return_value[1]

    return
```








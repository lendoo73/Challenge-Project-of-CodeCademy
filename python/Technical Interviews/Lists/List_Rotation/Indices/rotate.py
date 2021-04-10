# rotate list
# Constant space requirement
# return input list "rotated"
def boubble_up(my_list, pointer = 0):
  length = len(my_list)
  # base case:
  if pointer == length - 1:
    return my_list
  # recursive step:
  my_list[pointer], my_list[pointer + 1] = my_list[pointer + 1], my_list[pointer]
  return boubble_up(my_list, pointer + 1)


def rotate(my_list, num_rotations):
  length = len(my_list)
  rotation = num_rotations % length
  # boubble up:
  while num_rotations > 0:
    my_list = boubble_up(my_list)
    num_rotations -= 1
  return my_list

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['b', 'c', 'd', 'e', 'f', 'a'], 
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['b', 'c', 'd', 'e', 'f', 'a']
))

print("{0}\n should equal \n{1}\n {2}\n".format(
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['c', 'd', 'e', 'f', 'a', 'b'], 
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['c', 'd', 'e', 'f', 'a', 'b']
))

print("{0}\n should equal \n{1}\n {2}\n".format(
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], 
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']
))

print("{0}\n should equal \n{1}\n {2}\n".format(
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['e', 'f', 'a', 'b', 'c', 'd'], 
  rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['e', 'f', 'a', 'b', 'c', 'd']
))

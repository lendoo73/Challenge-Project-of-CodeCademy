# find rotation point 
# No time/space requirements
# return index of "rotation point" element

def rotation_point(rotated_list):
  min_val = rotated_list[0]
  min_index = 0
  for index, val in enumerate(rotated_list):
    if val < min_val:
      min_val = val
      min_index = index
  return min_index

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))

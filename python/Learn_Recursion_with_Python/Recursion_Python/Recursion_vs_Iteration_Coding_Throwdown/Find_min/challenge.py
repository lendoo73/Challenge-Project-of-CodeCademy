def find_min(my_list, min_val = None):
  # Base case: 
  if not len(my_list):
    return min_val
  # Recursive step:
  first_val = my_list[0]
  if min_val == None or first_val < min_val:
    min_val = first_val
  return find_min(my_list[1:], min_val)



# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)

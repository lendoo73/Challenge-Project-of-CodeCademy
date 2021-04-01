# Define build_bst() below...
def build_bst(my_list):
  length = len(my_list)
  # base case:
  if not length:
    return "No Child"
  
  middle_idx = length // 2
  middle_value = my_list[middle_idx]
  print(f"Middle index: {middle_idx}")
  print(f"Middle value: {middle_value}")

  # recursive step:
  tree_node = {
    "data": middle_value,
    "left_child": build_bst(my_list[ : middle_idx]),
    "right_child": build_bst(my_list[middle_idx + 1 : ])
  }
  
  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"

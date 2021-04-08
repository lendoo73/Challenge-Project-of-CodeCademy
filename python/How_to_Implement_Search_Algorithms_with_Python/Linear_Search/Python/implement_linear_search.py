def linear_search(search_list, target_value):
  for i in range(len(search_list)):
    if search_list[i] == target_value:
      return i
  
  raise ValueError(f"{target_value} not in list")

values = [54, 22, 46, 99]
print(linear_search(values, 22))
print(linear_search(values, 23))

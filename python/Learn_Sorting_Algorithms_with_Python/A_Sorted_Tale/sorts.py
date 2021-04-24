import random

# Fix the midday errors
# 4. add an argument 'comparison_function': 
def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      # 5. modify the comparison conditional statement:
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

# 11. Add comparison_function as the final argument:
def quicksort(list, start, end, comparison_function):
  # base case:
  if start >= end:
    return
  
  # recursive step:
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    # 13.:
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  # 12. 
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)

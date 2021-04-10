from timeit import timeit

## Rotate
def rotate(lst, degree):
  rotation = degree % len(lst)
  return lst[-rotation:] + lst[:-rotation]

def rev(lst, low, high):
  while low < high:
    lst[low], lst[high] = lst[high], lst[low]
    high -= 1
    low += 1
  return lst

def rotate_optimal(my_list, num_rotations):
  rev(my_list, 0, num_rotations - 1)
  rev(my_list, num_rotations, len(my_list) - 1)
  rev(my_list, 0, len(my_list) - 1)
  return my_list

print("NAIVE ROTATE: ")
print(timeit('rotate([i for i in range(1000)], 100)', number = 10, setup="from __main__ import rotate"))
print("SPACE OPTIMAL ROTATE: ")
print(timeit('rotate_optimal([i for i in range(1000)], 100)', number = 10, setup="from __main__ import rotate_optimal"))

## Rotate Point
def rotation_point(rotated_list):
  rotation_idx = 0
  for i in range(len(rotated_list)):
    if rotated_list[i] < rotated_list[rotation_idx]:
      rotation_idx = i
  return rotation_idx

def rotation_point_optimal(rotated_list):
  low = 0
  high = len(rotated_list) - 1
  while low <= high:
    mid = (low + high) // 2
    mid_next = (mid + 1) % len(rotated_list)
    mid_previous = (mid - 1) % len(rotated_list)
    
    if (rotated_list[mid] < rotated_list[mid_previous]) and (rotated_list[mid] < rotated_list[mid_next]):
      return mid
    elif rotated_list[mid] < rotated_list[high]:
      high = mid - 1
    else:
      low = mid + 1

print("\nNAIVE ROTATE POINT: ")
print(timeit('rotation_point([i for i in range(1000)])', number = 10, setup="from __main__ import rotation_point"))
print("TIME OPTIMAL ROTATE POINT: ")
print(timeit('rotation_point_optimal([i for i in range(1000)])', number = 10, setup="from __main__ import rotation_point_optimal"))

## Duplicates
def remove_duplicates(dupe_list):
  unique_values = []
  for el in dupe_list:
    if el not in unique_values:
      unique_values.append(el)
  return unique_values


def move_duplicates_optimal(dupe_list):
  unique_idx = 0
  for i in range(len(dupe_list) - 1):
    if dupe_list[i] != dupe_list[i + 1]:
      dupe_list[i], dupe_list[unique_idx] = dupe_list[unique_idx], dupe_list[i]
      unique_idx += 1
  dupe_list[unique_idx], dupe_list[len(dupe_list) - 1] = dupe_list[len(dupe_list) - 1], dupe_list[unique_idx]
  return unique_idx

print("\nNAIVE REMOVE DUPLICATES: ")
print(timeit('remove_duplicates([i + i for i in range(1000)])', number = 10, setup="from __main__ import remove_duplicates"))
print("SPACE OPTIMAL REMOVE DUPLICATES: ")
print(timeit('move_duplicates_optimal([i + i for i in range(1000)])', number = 10, setup="from __main__ import move_duplicates_optimal"))

## Max Sub Sum
def maximum_sub_sum(my_list):
  max_sum = my_list[0]
  for i in range(len(my_list)):
    for j in range(i, len(my_list)):
      sub_sum = sum(my_list[i:j + 1])
      if sub_sum > max_sum:
        max_sum = sub_sum
  return max_sum

def maximum_sub_sum_optimal(my_list):
  if max(my_list) < 0:
    return max(my_list)
  
  max_sum = 0
  max_sum_tracker = 0
  for i in range(len(my_list)):
    max_sum_tracker += my_list[i]
    if max_sum_tracker < 0:
      max_sum_tracker = 0
    if max_sum_tracker > max_sum:
      max_sum = max_sum_tracker
    
  return max_sum

print("\nNAIVE MAX SUB-SUM: ")
print(timeit('maximum_sub_sum([i for i in range(200)])', number = 10, setup="from __main__ import maximum_sub_sum"))
print("SPACE OPTIMAL REMOVE DUPLICATES: ")
print(timeit('maximum_sub_sum_optimal([i for i in range(200)])', number = 10, setup="from __main__ import maximum_sub_sum_optimal"))

## Pair Sum
def pair_sum(my_list, target):
  for i in range(len(my_list)):
    for j in range(i, len(my_list)):
      if my_list[i] + my_list[j] == target:
        return [i, j]
  return None

def pair_sum_optimal(my_list, target):
  comp = {}
  index = {}
  for i in range(len(my_list)):
    half = comp.get(my_list[i], None)
    if half is not None:
      return [index[half], i]
    comp[target - my_list[i]] = my_list[i]
    index[my_list[i]] = i
    
    
print("\nNAIVE PAIR SUM: ")
print(timeit('pair_sum([i for i in range(1000)], -1)', number = 10, setup="from __main__ import pair_sum"))
print("TIME OPTIMAL PAIR SUM: ")
print(timeit('pair_sum_optimal([i for i in range(1000)], -1)', number = 10, setup="from __main__ import pair_sum_optimal"))

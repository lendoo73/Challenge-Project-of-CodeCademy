from time import time

####### TEST INPUTS HERE
# 1.:
small = [1, 0, 1]
# 2.:
medium = [4, 2, 1, 3, 0, 1, 2]
# 3.:
edge_case = [0, 2, 0]

####### NAIVE SOLUTION HERE
# 4.:
def rain_water(histogram):
  # histogram: a Python list of positive integers.
  # 5.:
  # 11.:
  total_water = 0
  for i in range(1, len(histogram) - 1):
    # 6.:
    left_values = histogram[: i]
    left_max = max(left_values)
    # 7.:
    #print("Left max is: {0}".format(left_max))
    # 8.:
    right_values = histogram[i :]
    right_max = max(right_values)
    # 9.:
    #print("Right max is: {0}".format(right_max))
    # 10.: 
    fill_mark = min(left_max, right_max)
    # 12.:
    # 13.:
    current_value = histogram[i] 
    result = fill_mark - current_value
    # 14.:
    if result > 0:
      total_water += result
  return total_water

#print("small: ", rain_water(small))
#print("medium", rain_water(medium))
#print("edge_case", rain_water(edge_case))

####### OPTIMIZED SOLUTION HERE
def optimized_rain_water(histogram):
  # 21.:
  total = 0
  # 18.:
  max_value = histogram[0]
  # 19.:
  left_maxes = []
  for val in histogram:
    if val > max_value: max_value = val
    left_maxes.append(max_value)
  # 20.:
  max_value = histogram[-1]
  right_maxes = []
  for i in range(len(histogram) - 1, -1, -1):
    if histogram[i] > max_value: max_value = histogram[i]
    right_maxes.append(max_value)
  right_maxes.reverse()

  # 21.:
  for i in range(len(histogram)):
    total += min(left_maxes[i], right_maxes[i]) - histogram[i]
  
  return total

#print("small: ", optimized_rain_water(small))
#print("medium", optimized_rain_water(medium))
#print("edge_case", optimized_rain_water(edge_case))
####### BENCHMARKING HERE
# 15.:
start = time()
# 16.:
rain_water(small)
rain_water(medium)
rain_water(edge_case)
current_time = time()
result1 = current_time - start
#print("Naive solution", result1)
# 22.:
start = time()
optimized_rain_water(small)
optimized_rain_water(medium)
optimized_rain_water(edge_case)
current_time = time()
result2 = current_time - start
#print("Optimized solution", result2)
#print("Is Naive solution slower than the Optimized? ", result1 > result2)

# 23.:
large = [i for i in range(10000)]

start = time()
# 16.:
rain_water(large)
current_time = time()
result1 = current_time - start
#print("Naive solution", result1)


start = time()
optimized_rain_water(large)
current_time = time()
result2 = current_time - start
print("Optimized solution", result2)
print("Is Naive solution slower than the Optimized? ", result1 > result2)

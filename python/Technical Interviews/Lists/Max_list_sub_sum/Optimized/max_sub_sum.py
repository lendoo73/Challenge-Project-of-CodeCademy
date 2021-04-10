# max sub sum
# linear time, constant space requirements
# return maximum contiguous sum in list

def maximum_sub_sum(my_list):
  max_my_list = max(my_list)
  if max_my_list < 0: return max_my_list

  max_sum = 0
  max_sum_tracker = 0

  for val in my_list:
    max_sum_tracker += val
    if max_sum_tracker < 0: max_sum_tracker = 0
    if max_sum_tracker > max_sum: 
      max_sum = max_sum_tracker
  
  return max_sum

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, 2, 3, 4, 5]), 15, maximum_sub_sum([1, 2, 3, 4, 5]) == 15))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]), -1, maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]) == -1))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, -7, 2, 15, -11, 2]), 17, maximum_sub_sum([1, -7, 2, 15, -11, 2]) == 17))

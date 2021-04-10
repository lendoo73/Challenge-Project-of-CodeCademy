# max sub sum
# no time/space requirements
# return maximum contiguous sum in list

def maximum_sub_sum(my_list):
  max_sum = my_list[0]

  for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
      copy = my_list[i : j + 1]
      sub_max = sum(copy)
      if sub_max > max_sum:
        max_sum = sub_max
  
  return max_sum 

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, 2, 3, 4, 5]), 15, maximum_sub_sum([1, 2, 3, 4, 5]) == 15))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]), -1, maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]) == -1))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, -7, 2, 15, -11, 2]), 17, maximum_sub_sum([1, -7, 2, 15, -11, 2]) == 17))

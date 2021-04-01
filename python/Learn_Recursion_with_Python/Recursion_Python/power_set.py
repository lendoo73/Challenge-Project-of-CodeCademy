def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU', "KISEGÍTŐ"]
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
    print(set)

def equal_dimension(pt1, pt2):
  if len(pt1) == len(pt2):
    return True

def euclidean_distance(pt1, pt2):
  
  if not equal_dimension(pt1, pt2):
    return "ERROR: Different number of dimensions!"

  distance = 0
  for i in range(len(pt1)):
    difference = (pt2[i] - pt1[i]) ** 2
    distance += difference

  return distance ** 0.5

def manhattan_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += abs(pt1[i] - pt2[i])
  return distance

print("Euclidean  distance:")
print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))
print(euclidean_distance([2, 3, 4], [1, 2]))

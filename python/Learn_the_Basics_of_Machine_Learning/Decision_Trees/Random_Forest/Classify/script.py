from tree import build_tree, print_tree, car_data, car_labels, classify
import random
random.seed(4)

# The features are the price of the car, the cost of maintenance, the number of doors, the number of people the car can hold, the size of the trunk, and the safety rating
unlabeled_point = [
  'high',    # the price of the car
  'vhigh',   # the cost of maintenance
  '3',       # the number of doors
  'more',    # the number of people the car can hold
  'med',     # the size of the trunk
  'med'      # the safety rating
]

# Let’s make 20 trees and record the prediction of each one!
predictions = []
for i in range(20):
  indices = [random.randint(0, 999) for i in range(1000)]
  data_subset = [car_data[index] for index in indices]
  labels_subset = [car_labels[index] for index in indices]
  subset_tree = build_tree(data_subset, labels_subset)

  predictions.append(classify(unlabeled_point, subset_tree))

print(predictions)
# find the most common prediction
final_prediction = max(predictions, key=predictions.count)
print(final_prediction)

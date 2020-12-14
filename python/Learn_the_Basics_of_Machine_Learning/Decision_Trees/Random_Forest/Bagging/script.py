from tree import build_tree, print_tree, car_data, car_labels
import random

random.seed(4)

tree = build_tree(car_data, car_labels)

#print_tree(tree)
indices = [random.randint(0, 999) for i in range(1000)]

data_subset = []
labels_subset = []
for index in indices:
  data_subset.append(car_data[index])
  labels_subset.append(car_labels[index])

subset_tree = build_tree(data_subset, labels_subset)
print_tree(subset_tree)

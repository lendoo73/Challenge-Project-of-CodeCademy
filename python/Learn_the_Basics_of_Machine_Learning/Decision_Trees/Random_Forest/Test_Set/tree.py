import operator
from collections import Counter
import random
import numpy as np
np.random.seed(1)
random.seed(1)

def split(dataset, labels, column):
    data_subsets = []
    label_subsets = []
    counts = list(set([data[column] for data in dataset]))
    counts.sort()
    for k in counts:
        new_data_subset = []
        new_label_subset = []
        for i in range(len(dataset)):
            if dataset[i][column] == k:
                new_data_subset.append(dataset[i])
                new_label_subset.append(labels[i])
        data_subsets.append(new_data_subset)
        label_subsets.append(new_label_subset)
    return data_subsets, label_subsets

def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity

def information_gain(starting_labels, split_labels):
  info_gain = gini(starting_labels)
  for subset in split_labels:
    info_gain -= gini(subset) * len(subset)/len(starting_labels)
  return info_gain

class Leaf:
    def __init__(self, labels, value):
        self.labels = Counter(labels)
        self.value = value

class Internal_Node:
    def __init__(self,
                 feature,
                 branches,
                 value):
        self.feature = feature
        self.branches = branches
        self.value = value

def find_best_split_subset(dataset, labels, num_features):
    features = np.random.choice(6, 3, replace=False)
    best_gain = 0
    best_feature = 0
    for feature in features:
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_feature, best_gain

def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    for feature in range(len(dataset[0])):
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_feature, best_gain

def make_single_tree(data, labels, value = ""):
  best_feature, best_gain = find_best_split(data, labels)
  if best_gain < 0.00000001:
    return Leaf(Counter(labels), value)
  data_subsets, label_subsets = split(data, labels, best_feature)
  branches = []
  for i in range(len(data_subsets)):
    branch = make_single_tree(data_subsets[i], label_subsets[i], data_subsets[i][0][best_feature])
    branches.append(branch)
  return Internal_Node(best_feature, branches, value)

def build_tree_forest(data,labels, n_features, value=""):
    best_feature, best_gain = find_best_split_subset(data, labels, n_features)
    if best_gain < 0.00000001:
      return Leaf(Counter(labels), value)
    data_subsets, label_subsets = split(data, labels, best_feature)
    branches = []
    for i in range(len(data_subsets)):
      branch = build_tree_forest(data_subsets[i], label_subsets[i], n_features, data_subsets[i][0][best_feature])
      branches.append(branch)
    return Internal_Node(best_feature, branches, value)

def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""
    question_dict = {0: "Buying Price", 1:"Price of maintenance", 2:"Number of doors", 3:"Person Capacity", 4:"Size of luggage boot", 5:"Estimated Saftey"}
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + str(node.labels))
        return

    # Print the question at this node
    print (spacing + "Splitting on " + question_dict[node.feature])

    # Call this function recursively on the true branch
    for i in range(len(node.branches)):
        print (spacing + '--> Branch ' + node.branches[i].value+':')
        print_tree(node.branches[i], spacing + "  ")

def make_cars():
    f = open("car.data", "r")
    cars = []
    for line in f:
        cars.append(line.rstrip().split(","))
    return cars

def change_data(data):
    dicts = [{'vhigh' : 1.0, 'high' : 2.0, 'med' : 3.0, 'low' : 4.0},
    {'vhigh' : 1.0, 'high' : 2.0, 'med' : 3.0, 'low' : 4.0},
    {'2' : 1.0, '3' : 2.0, '4' : 3.0, '5more' : 4.0},
    {'2' : 1.0, '4' : 2.0, 'more' : 3.0},
    {'small' : 1.0, 'med' : 2.0, 'big' : 3.0},
    {'low' : 1.0, 'med' : 2.0, 'high' : 3.0}]

    for row in data:
        for i in range(len(dicts)):
            row[i] = dicts[i][row[i]]

    return data


def classify(datapoint, tree):
  if isinstance(tree, Leaf):
    items = list(tree.labels.items()) 
    items.sort()
    return max(items, key=operator.itemgetter(1))[0]

  value = datapoint[tree.feature]
  for branch in tree.branches:
    if branch.value == value:
      return classify(datapoint, branch)
  #return classify(datapoint, tree.branches[random.randint(0, len(tree.branches)-1)])


cars = make_cars()
random.shuffle(cars)
car_data = [x[:-1] for x in cars]
car_labels = [x[-1] for x in cars]
# car_data = car_data[:500]
# car_labels = car_labels[:500]


training_data = car_data[:int(len(car_data)*0.8)]
training_labels = car_labels[:int(len(car_data)*0.8)]

testing_data = car_data[int(len(car_data)*0.8):]
testing_labels = car_labels[int(len(car_data)*0.8):]

def make_random_forest(n, training_data, training_labels):
    trees = []
    for i in range(n):
        indices = [random.randint(0, len(training_data)-1) for x in range(len(training_data))]

        training_data_subset = [training_data[index] for index in indices]
        training_labels_subset = [training_labels[index] for index in indices]

        tree = build_tree_forest(training_data_subset, training_labels_subset, 2)
        trees.append(tree)
    return trees

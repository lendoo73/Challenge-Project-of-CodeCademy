from collections import Counter
import random
random.seed(1)

def make_cars():
    f = open("car.data", "r")
    cars = []
    for line in f:
        cars.append(line.rstrip().split(","))
    return cars
  
cars = make_cars()
random.shuffle(cars)
cars = cars[:1000]
car_data = [x[:-1] for x in cars]
car_labels = [x[-1] for x in cars]

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
        self.predictions = Counter(labels)
        self.value = value

class Decision_Node:


    def __init__(self,
                 question,
                 branches, value):
        self.question = question
        self.branches = branches
        self.value = value
  
def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""
    question_dict = {0: "Buying Price", 1:"Price of maintenance", 2:"Number of doors", 3:"Person Capacity", 4:"Size of luggage boot", 5:"Estimated Saftey"}
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print (spacing + question_dict[node.question])

    # Call this function recursively on the true branch
    for i in range(len(node.branches)):
        print (spacing + '--> Branch ' + node.branches[i].value+':')
        print_tree(node.branches[i], spacing + "  ")
        
def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    for feature in range(len(dataset[0])):
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_gain, best_feature
  
def build_tree(rows, labels, value = ""):
    gain, question = find_best_split(rows, labels)
    if gain == 0:
        return Leaf(labels, value)
    data_subsets, label_subsets = split(rows, labels, question)
    branches = []
    for i in range(len(data_subsets)):
        branch = build_tree(data_subsets[i], label_subsets[i], data_subsets[i][0][question])
        branches.append(branch)
    return Decision_Node(question, branches, value)

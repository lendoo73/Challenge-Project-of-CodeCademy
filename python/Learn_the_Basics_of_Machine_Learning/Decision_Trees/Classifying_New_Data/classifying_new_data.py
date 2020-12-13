from tree import *
import operator

test_point = ['vhigh', 'low', '3', '4', 'med', 'med']

print_tree(tree)

def classify(datapoint, tree):
  if isinstance(tree, Leaf):
    return max(tree.labels.items(), key = operator.itemgetter(1))[0]

  value = datapoint[tree.feature]
  for branch in tree.branches:
    if branch.value == value:
      return classify(datapoint, branch)

result = classify(test_point, tree)
print(result)

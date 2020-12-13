from collections import Counter

labels = ["unacc", "unacc", "acc", "acc", "good", "good"]
labels = ["unacc","unacc","unacc", "good", "vgood", "vgood"]
#labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc"]
"""
impurity = 1

label_counts = Counter(labels)
print(label_counts)

for label in label_counts:
  probability_of_label = label_counts[label] / len(labels)
  impurity = impurity - probability_of_label ** 2
"""
def gini(labels):
  label_keys = set(labels)
  impurity = 1
  for label in label_keys:
    probability_of_label = labels.count(label) / len(labels)
    impurity = impurity - probability_of_label ** 2
  return impurity

print(gini(labels))
#print(impurity)

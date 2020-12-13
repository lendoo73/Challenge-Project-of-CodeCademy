labels = ["unacc", "unacc", "acc", "acc", "good", "good"]
labels = ["unacc","unacc","unacc", "good", "vgood", "vgood"]
#labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc"]

def gini(labels):
  label_keys = set(labels)
  total_number_of_labels = len(labels)
  impurity = 1
  for label in label_keys:
    probability_of_label = labels.count(label) / total_number_of_labels
    impurity = impurity - probability_of_label ** 2
  return impurity

print(gini(labels))

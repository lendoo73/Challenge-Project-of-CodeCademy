import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Explore the data:
print("\n________________________________")
print("Explore the data:")
breast_cancer_data = load_breast_cancer()
print("Features:")
for i in range(len(breast_cancer_data.data[0])):
  print(f"{breast_cancer_data.feature_names[i]}: {breast_cancer_data.data[0][i]}")
  pass

print("\nLabels:")
print(f" - {breast_cancer_data.target_names[0]}: {breast_cancer_data.target[0]}")
print(f" - {breast_cancer_data.target_names[-1]}: {breast_cancer_data.target[-1]}")
print(len(breast_cancer_data.data))
print(len(breast_cancer_data.target))

# Splitting the data into Training and Validation Sets:
print("\n________________________________")
print("Splitting the data into Training and Validation Sets:")
training_data, validation_data, training_labels, validation_labels = train_test_split(
  breast_cancer_data.data,   # The data you want to split
  breast_cancer_data.target, # The labels associated with that data
  test_size = 0.2, 
  random_state = 100
)

print(len(training_data))
print(len(training_labels))
print(len(breast_cancer_data.data) * 0.8)

# Running the classifier:
print("\n________________________________")
print("Running the classifier:")

best_score = 0
best_K = 0
accuracies = []
k_list = list(range(1, 101))
for k in k_list:
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(training_data, training_labels)

  score = classifier.score(validation_data, validation_labels)
  accuracies.append(score)
  #print(f"K: {k} - score: {score}")
  if best_score < score:
    best_score = score
    best_K = k

print(f"The best K is: {best_K} with score: {best_score}")
print(accuracies[55])

# # Graphing the results:
print("\n________________________________")
print("Graphing the results:")
plt.plot(k_list, accuracies)
plt.xlabel("K")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()


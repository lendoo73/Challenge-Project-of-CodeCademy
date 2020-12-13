import codecademylib3_seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Investigate the Data
flags = pd.read_csv(
  "flags.csv",
  header = 0
)
columns = flags.columns.values
print(flags.head())

# Creating Your Data and Labels
labels = flags.Landmass
data = flags.iloc[:, 10 : 17]
data = flags[[
  "Red", "Green", "Blue", "Gold",
 "White", "Black", "Orange",
 "Circles",
"Crosses","Saltires","Quarters","Sunstars",
"Crescent","Triangle"
]]

data = flags[[
  #"Area",
  #"Population",
  #"Bars",
  #"Stripes",
  #"Colors",
  "Red", 
  "Green", 
  "Blue", 
  "Gold",
  "White", 
  "Black", 
  #"Orange",
  #"Circles",
  "Crosses",
  #"Saltires",
  #"Quarters",
  "Sunstars",
  #"Crescent",
  "Triangle",
  #"Icon", 
  #"Animate", 
  #"Text"
]]

train_data, test_data, train_labels, test_labels = train_test_split(
  data,
  labels,
  random_state = 1
)

# Make and Test the Model
scores = []
best = {
  "depth": 0,
  "accuracy": 0,
  "max_depth": 21
}

for i in range(1, 21):
  tree = DecisionTreeClassifier(
    random_state = 1,
    max_depth = i
  )

  tree.fit(train_data, train_labels)
  max_depth = tree.tree_.max_depth
  if max_depth == best["max_depth"]:
    break
  else:
    best["max_depth"] = max_depth

  accuracy = tree.score(test_data, test_labels)
  scores.append(accuracy)
  if accuracy > best["accuracy"]:
    best["accuracy"] = accuracy
    best["depth"] = i

best["accuracy"] = "{:.2f}".format(best["accuracy"])

best["max_depth"] = best["max_depth"] + 1

plt.plot(
  range(1, best["max_depth"]),
  scores,
  label = f"Best accuracy: {best['accuracy']}"
)
plt.title("Depth vs. Accuracy")
plt.xticks(range(1, best["max_depth"], 2))
plt.xlabel("depth")
plt.ylabel("accuracy")
plt.axvline(
  x = best['depth'], 
  c = "red",
  linestyle = "--",
  label = f"Depth: {best['depth']}"
)
plt.legend()
plt.show()

print(f"The best depth: {best['depth']}\nThe best accuracy: {best['accuracy']}")

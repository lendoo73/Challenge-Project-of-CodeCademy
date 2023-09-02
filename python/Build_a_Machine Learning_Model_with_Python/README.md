# [The Machine Learning Process](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/the-ml-process)
Learn the general structure of how to approach Machine Learning problems in a methodical way.

# [Supervised vs. Unsupervised](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/machine-learning-supervised-vs-unsupervised)
Introduction to the two main classes of algorithms in Machine Learning — Supervised Learning & Unsupervised Learning.

# [What is Scikit-Learn?](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/scikit-learn)
Open-source ML library for Python. Built on NumPy, SciPy, and Matplotlib.

# [Scikit-Learn Cheatsheet](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/scikit-learn-cheatsheet)

## [Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

```py
# Import and create the model:
from sklearn.linear_model import LinearRegression
 
your_model = LinearRegression()

# Fit:
your_model.fit(x_training_data, y_training_data)

print(your_model.coef_)           # contains the coefficients
print(your_model.intercept_)      # contains the intercept

# Predict:
predictions = your_model.predict(your_x_data)

print(predictions.score())        # returns the coefficient of determination R²
```

Visualize
```py
import matplotlib.pyplot as plt

plt.scatter(x_training_data, y_training_data) 
plt.plot([min(x_training_data), max(x_training_data)], [min(predictions), max(predictions)], color='red')  # line of bets fit in red
plt.show()
```

## [Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)
```py
# Import and create the model:
from sklearn.naive_bayes import MultinomialNB
 
your_model = MultinomialNB()

# Fit:
your_model.fit(x_training_data, y_training_data)

# Predict:
# Returns a list of predicted classes - one prediction for every data point
predictions = your_model.predict(your_x_data)
 
# For every data point, returns a list of probabilities of each class
probabilities = your_model.predict_proba(your_x_data)
```

## [K-Nearest Neighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)
```py
# Import and create the model:
from sklearn.neigbors import KNeighborsClassifier
 
your_model = KNeighborsClassifier()

# Fit:
your_model.fit(x_training_data, y_training_data)

# Predict:
# Returns a list of predicted classes - one prediction for every data point
predictions = your_model.predict(your_x_data)
 
# For every data point, returns a list of probabilities of each class
probabilities = your_model.predict_proba(your_x_data)
```

## [K-Means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
```py
# Import and create the model:
from sklearn.cluster import KMeans
 
your_model = KMeans(
  n_clusters = 4,           # number of clusters to form and number of centroids to generate
  init = "random",          # method for initialization
                            #      "k-means++": K-Means++; default value
                            #      "random": K-Means
  random_state = 42         # the seed used by the random number generator [optional]
)

# Fit:
your_model.fit(x_training_data)

# Predict:
predictions = your_model.predict(your_x_data)
```

## [Validating the Model](https://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics)

### Import and print accuracy, recall, precision, and F1 score:
```py
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
 
print(accuracy_score(true_labels, guesses))
print(recall_score(true_labels, guesses))
print(precision_score(true_labels, guesses))
print(f1_score(true_labels, guesses))
```

### Import and print the confusion matrix:
```py
from sklearn.metrics import confusion_matrix
 
print(confusion_matrix(true_labels, guesses))
```

## [Training Sets and Test Sets](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
```py
from sklearn.model_selection import train_test_split
 
x_train, x_test, y_train, y_test = train_test_split(
  x, 
  y, 
  train_size = 0.8,           # the proportion of the dataset to include in the train split
  test_size = 0.2,            # the proportion of the dataset to include in the test split
  random_state: 42            # the seed used by the random number generator [optional]
)
```

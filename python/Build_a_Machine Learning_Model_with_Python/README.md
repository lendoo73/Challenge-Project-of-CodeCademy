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

### Visualize
```py
import matplotlib.pyplot as plt

plt.scatter(x_training_data, y_training_data) 
# line of bets fit in red
plt.plot(
    [min(x_training_data), max(x_training_data)],
    [min(predictions), max(predictions)],
    color='red'
)
plt.show()
```

```˙py
plt.plot(x_training_data, your_model.coef_[0] * x_training_data + your_model.intercept_);
```

### Evaluating

#### Calculate the Sum of Squared Errors (SSE)

This measures how close the model predictions are to the true values.

```py
sse = sum( (y_training_data - predictions) ** 2 )
```

#### Calculate the Total Sum of Squars)

```py
tse = sum( (y_training_data - np.mean(y_training_data)) ** 2 )
```

#### Calculate Coefficient of determination ($R^2$) 

It describes how well the model represents the data.

```py
r_squared = 1 - (sse / tse)
```

#### Calculate the Mean Squared Errors (MSE)

```py
mse = np.mean( (y_training_data - predictions) ** 2 )
```

#### Calculate F-statistic

J is the number of features.
N is number of observations

```py
J = x_training_data.shape[1] if len(x_training_data.shape) > 1 else 1
N = len(x_training_data)
f_statistic = (tse / J) / (sse / (N - J - 1))
```

#### Hypothesis tests

```py
import statsmodels.api as sm

X = sm.add_constant(x_training_data)
results = sm.OLS(y_training_data, x_training_data).fit()

# Get the overall results for the multivariate model
print(results.summary())

# Get only the results for the F-statistic and it's corresponding p-value
F = np.identity(len(results.params))
F = F[1:,:]

print(results.f_test(F))
```

## [Linear Regression OLS](https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html)

```py
from statsmodels.regression.linear_model import OLS

model = OLS(y, X)
results = model.fit()

# Get the overall results for the multivariate model
print(results.summary())

bias = results.params[0]
weights = results.params[1:]
r_squared = results.rsquared

# Predict:
predictions = results.fittedvalues
# or
predictions = results.predict()
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

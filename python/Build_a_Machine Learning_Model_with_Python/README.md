# [The Machine Learning Process](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/the-ml-process)
Learn the general structure of how to approach Machine Learning problems in a methodical way.

# [Supervised vs. Unsupervised](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/machine-learning-supervised-vs-unsupervised)
Introduction to the two main classes of algorithms in Machine Learning — Supervised Learning & Unsupervised Learning.

# [What is Scikit-Learn?](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/scikit-learn)
Open-source ML library for Python. Built on NumPy, SciPy, and Matplotlib.

# [Scikit-Learn Cheatsheet](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-machine-learning-skill-path/modules/introduction-to-machine-learning-skill-path/articles/scikit-learn-cheatsheet)

## [Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

```
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

## [Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)

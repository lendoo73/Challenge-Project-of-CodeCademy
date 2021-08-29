#### CHOOSING A LINEAR REGRESSION MODEL
# [Training and Test Sets](https://www.codecademy.com/courses/linear-regression-mssp/lessons/choosing-a-linear-regression-model/exercises/training-and-test-sets)

Another way of choosing a model to make predictions for new data (also called out-of-sample prediction) is by using training and test datasets. 
The idea is that we only use PART of our data to fit the model, then we see how well the model performs in predicting the outcome of interest for the rest of our data. 
The process is as follows:
* First, we split our data into two subsets: a **training set** and a **test set**. Often, the *training set is a larger** proportion of the data.
* In other Python libraries, there are built-in functions to split a dataframe, 
but for the sake of understanding, we’ll do it explicitly here by randomly sampling from a list of row indices:

```py
import numpy as np
 
# Create a list of indices
indices = range(len(rentals))
 
# Determine the size of the training set (s)
s = int(0.8 * len(indices))
 
# Randomly select 80% of the indices
train_ind = np.random.choice(indices, size = s, replace = False)
 
# Create a list of the remaining 20% of indices
test_ind = list(set(indices) - set(train_ind))
 
# Split the data into the training and test sets
rentals_train = rentals.iloc[train_ind]
rentals_test = rentals.iloc[test_ind]
```

* Next, we fit the models we want to compare using the training set data only:

```py
model1 = sm.OLS.from_formula(
    'rent ~ bedrooms + bathrooms + size_sqft + min_to_subway + floor', 
    data = rentals_train
).fit()
 
model2 = sm.OLS.from_formula(
    'rent ~ bedrooms + bathrooms + size_sqft + min_to_subway + floor + borough', 
    data = rentals_train
).fit()
```

* Then, we use those models to predict the rental price for the apartments in the test set:

```py
fitted1 = model1.predict(rentals_test)
fitted2 = model2.predict(rentals_test)
```

* Finally, we can compare the predicted rents to the true rents in the test set and use a metric to determine how well each model performed.
* In this example, we’ll use a metric called predictive root mean squared error (PRMSE), which is exactly what the name sounds like: 
the square root of the mean squared difference between predicted and true values of the outcome variable. 
A **smaller PRMSE** means that the model performed **better** (the predicted values were more similar to the true values):

```py
true = rentals_test.rent
prmse1 = np.mean((true - fitted1) ** 2) ** 0.5
prmse2 = np.mean((true - fitted2) ** 2) ** 0.5
print(prmse1) #output: 1326.258
print(prmse2) #output: 1224.269
```
Based on this metric, we would choose the second model over the first one because it has a smaller PRMSE.

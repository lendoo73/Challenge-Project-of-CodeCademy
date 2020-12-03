# [Introduction to Multiple Linear Regression](https://www.codecademy.com/courses/machine-learning/lessons/multiple-linear-regression-streeteasy/exercises/introduction)
Linear regression is useful when we want to predict the values of a variable from its relationship with other variables.
There are two different types of linear regression models: 
* simple linear regression and 
* multiple linear regression

In predicting the price of a home, one factor to consider is the size of the home. 
The relationship between those two variables, price and size, is important, but there are other variables that factor in to pricing a home: 
location, air quality, demographics, parking, and more.
When making predictions for price, our dependent variable, we’ll want to use multiple independent variables. 
To do this, we’ll use Multiple Linear Regression. 
**Multiple Linear Regression** uses two or more independent variables to predict the values of the dependent variable.
It is based on the following equation:
### *y = b + m<sub>1</sub>x<sub>1</sub> + m<sub>2</sub>x<sub>2</sub> + ... + m<sub>n</sub>x<sub>n</sub>*

# [Training Set vs. Test Set](https://www.codecademy.com/courses/machine-learning/lessons/multiple-linear-regression-streeteasy/exercises/training-vs-test)
We have to split our dataset into:
* **Training set:** the data used to fit the model
* **Test set:** the data partitioned away at the very start of the experiment (to provide an unbiased evaluation of the model)

 Putting 80% of your data in the training set and 20% of your data in the test set is a good place to start.
 ```
 from sklearn.model_selection import train_test_split
 
x_train, x_test, y_train, y_test = train_test_split(
  x, 
  y, 
  train_size = 0.8, 
  test_size = 0.2
)
 ```
* `train_size`: the proportion of the dataset to include in the train split (between 0.0 and 1.0)
* `test_size`: the proportion of the dataset to include in the test split (between 0.0 and 1.0)
* `random_state`: the seed used by the random number generator [optional]

To learn more, here is a [Training Set vs Validation Set vs Test Set article](https://www.codecademy.com/articles/training-set-vs-validation-set-vs-test-set).

# [Multiple Linear Regression: Scikit-Learn](https://www.codecademy.com/courses/machine-learning/lessons/multiple-linear-regression-streeteasy/exercises/scikit-learn)
The steps for multiple linear regression in scikit-learn are identical to the steps for simple linear regression. 
We need to import LinearRegression from the linear_model module:
```
from sklearn.linear_model import LinearRegression
```
Then, create a LinearRegression model, and then fit it to your x_train and y_train data:
```
mlr = LinearRegression()
 
mlr.fit(x_train, y_train)
```
We can also use the .predict() function to pass in x-values. It returns the y-values that this plane would predict:
```
y_predicted = mlr.predict(x_test)
```

# [Visualizing Results with Matplotlib](https://www.codecademy.com/courses/machine-learning/lessons/multiple-linear-regression-streeteasy/exercises/visualization)
Graphs can be created using Matplotlib’s pyplot module. 
```
# Create a scatter plot
plt.scatter(x, y, alpha=0.4)
 
# Create x-axis label and y-axis label
plt.xlabel("the x-axis label")
plt.ylabel("the y-axis label")
 
# Create a title
plt.title("title!")
 
# Show the plot
plt.show()
```

# [Multiple Linear Regression Equation](https://www.codecademy.com/courses/machine-learning/lessons/multiple-linear-regression-streeteasy/exercises/equation)
Now that we have implemented Multiple Linear Regression, we will learn how to tune and evaluate the model.

### Equation 6.1 
The equation for multiple linear regression that uses two independent variables is this:
*y = b + m<sub>1</sub>x<sub>1</sub> + m<sub>2</sub>x<sub>2</sub>

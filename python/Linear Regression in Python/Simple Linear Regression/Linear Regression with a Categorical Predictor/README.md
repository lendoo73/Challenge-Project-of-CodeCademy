# [Linear Regression with a Categorical Predictor](https://www.codecademy.com/courses/linear-regression-mssp/articles/linear-regression-with-a-categorical-predictor)

Learn how to fit and interpret a linear model with a categorical predictor that has more than two categories.

## Introduction

Linear regression is a machine learning technique that can be used to model the relationship between a quantitative variable and some other variable(s). 
Those other variables can be either quantitative (e.g., height or salary) or categorical (e.g., job industry or hair color). 
However, if we want to include categorical predictors in a linear regression model, we need to treat them a little differently than quantitative variables. 
This article will explore the implementation and interpretation of a single categorical predictor with more than two categories.

## The Data

As an example, we’ll use a [dataset from StreetEasy](https://github.com/Codecademy/datasets/tree/master/streeteasy) 
that contains information about housing rentals in New York City. 
For now, we’ll only focus on two columns of this dataset:
* **rent**: the rental price of each apartment
* **borough**: the borough that the apartment is located in, with three possible values (**'Manhattan'**, **'Brooklyn'**, and **'Queens'**)

The first five rows of data are printed below:
```py
import pandas as pd
rentals = pd.read_csv('rentals.csv')
print(rentals.head(5))
```

| | rent |	borough |
| ---- | ---- | ---- |
| 0 | 5295 |	Brooklyn |
| 1 |	4020 |	Manhattan |
| 2 |	16000 |	Manhattan |
| 3 |	3150 |	Queens |
| 4 |	2955 |	Queens |

## The X Matrix

To understand how we can fit a regression model with a categorical predictor, 
it’s useful to walk through what happens when we use `statsmodels.api.OLS.from_formula()` to create a model. 
When we pass a formula to this function (like `'weight ~ height'` or `'rent ~ borough'`), it actually creates a new data set, which we don’t see. 
This new data set is often referred to as the *X matrix*, and it is used to fit the model.

When we use a quantitative predictor, the X matrix looks similar to the original data, but with an additional column of `1`s in front 
(the reasoning behind this column of `1`s is the subject of a future article — for now, no need to worry about it!). 
However, when we fit the model with a categorical predictor, something else happens: we end up with additional column(s) of `1`s and `0`s.

For example, let’s say we want to fit a regression predicting rent based on `borough`. 
We can see the X matrix for this model using `patsy.dmatrices()`, which is implemented behind the scenes in statsmodels:
```py
import pandas as pd
import patsy
 
rentals = pd.read_csv('rentals.csv')
y, X = patsy.dmatrices('rent ~ borough', rentals)
 
# Print out the first 5 rows of X
print(X[0:5])
```

Output:
```py
[[1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 0.]
 [1. 0. 1.]
 [1. 0. 1.]]
```

The first column is all `1`s, just like we would get for a quantitative predictor; but the second two columns were formed based on the `borough` variable. 
Remember that the first five values of the `borough` column looked like this:
|       |
| ---- |
| borough |
| Brooklyn |
| Manhattan |
| Manhattan |
| Queens |
| Queens |

Note that the second column of the X matrix `[0, 1, 1, 0, 0]` is an indicator variable for Manhattan: 
it is equal to `1` where the value of `borough` is `'Manhattan'` and `0` otherwise. 
Meanwhile, the third column of the X matrix (`[0, 0, 0, 1, 1]`) is an indicator variable for Queens: 
it is equal to `1` where the value of borough is `'Queens'` and `0` otherwise.

The X matrix does not contain an indicator variable for Brooklyn. 
That’s because this data set only contains three possible values of `borough`: `'Brooklyn'`, `'Manhattan'`, and `'Queens'`. 
In order to recreate the `borough` column, we only need two indicator columns — because any apartment that is not in `'Manhattan'` or `'Queens'` must be `'Brooklyn'`. 
For example, the first row of the X matrix has `0`s in both indicator columns, indicating that the apartment must be in Brooklyn. 
Mathematically, we say that a `'Brooklyn'` indicator creates collinearity in the X matrix. 
In regular English: a `'Brooklyn'` indicator does not add any new information.

Because `'Brooklyn'` is missing from the X matrix, it is the ***reference category*** for this model.

## Implementation and Interpretation

Let’s now fit a linear regression model using `statsmodels` and print out the model coefficients:
```py
import statsmodels.api as sm
model = sm.OLS.from_formula('rent ~ borough', rentals).fit()
print(model.params)
```

Output:
```
Intercept               3327.403751
borough[T.Manhattan]    1811.536627
borough[T.Queens]       -811.256430
dtype: float64
```

In the output, we see two different slopes: 
one for `borough[T.Manhattan]` and one for `borough[T.Queens]`, which are the two indicator variables we saw in the X matrix. 
We can use the intercept and two slopes to construct the following equation to predict rent:

### *rent = 3327.4 + 1811.5 * borough[T.Manhattan] - 811.3 * borough[T.Queens]*

To understand and interpret this equation, we can construct separate equations for each borough:

### Equation 1: Brooklyn

When an apartment is located in Brooklyn, both `borough[T.Manhattan]` and `borough[T.Queens]` will be equal to zero and the equation becomes:

\begin{aligned} rent = 3327.4 + 1811.5 * 0 - 811.3 * 0 \\ rent = 3327.4 \end{aligned} 

rent=3327.4+1811.5∗0−811.3∗0
rent=3327.4
​	 
In other words, the intercept is the predicted (average) rental price for an apartment in Brooklyn (the reference category).

Equation 2: Manhattan
When an apartment is located in Manhattan, borough[T.Manhattan] = 1 and borough[T.Queens] = 0. The equation becomes:

\begin{aligned} rent = 3327.4 + 1811.5 * 1 - 811.3 * 0 \\ rent = 3327.4 + 1811.5 \\ rent = 5138.9 \end{aligned} 
rent=3327.4+1811.5∗1−811.3∗0
rent=3327.4+1811.5
rent=5138.9
​	 
We see that the predicted (average) rental price for an apartment in Manhattan is 3327.4 + 1811.5: the intercept (which is the average price in Brooklyn) plus the slope on borough[T.Manhattan]. We can therefore interpret the slope on borough[T.Manhattan] as the difference in average rental price between apartments in Brooklyn (the reference category) and Manhattan.

Equation 3: Queens
When an apartment is located in Queens, borough[T.Manhattan] = 0 and borough[T.Queens] = 1. The equation becomes:

\begin{aligned} rent = 3327.4 + 1811.5 * 0 - 811.3 * 1 \\ rent = 3327.4 - 811.3 \\ rent = 2516.1 \end{aligned} 
rent=3327.4+1811.5∗0−811.3∗1
rent=3327.4−811.3
rent=2516.1
​	 
We see that the predicted (average) rental price for an apartment in Queens is 3327.4 - 811.3: the intercept (which is the average price in Brooklyn) plus the slope on borough[T.Queens] (which happens to be negative because Queens apartments are less expensive than Brooklyn apartments). We can therefore interpret the slope on borough[T.Queens] as the difference in average rental price between apartments in Brooklyn (the reference category) and Queens.

We can verify our understanding of all these coefficients by printing out the average rental prices by borough:

print(rentals.groupby('borough').mean())
Output:

                  rent
borough               
Brooklyn   3327.403751
Manhattan  5138.940379
Queens     2516.147321
The average prices in each borough come out to the exact same values that we predicted based on the linear regression model! For now, this may seem like an overly complicated way to recover mean rental prices by borough, but it is important to understand how this works in order to build up more complex linear regression models in the future.

Changing the Reference Category
In the example above, we saw that 'Brooklyn' was the default reference category (because it comes first alphabetically), but we can easily change the reference category in the model as follows:

model = sm.OLS.from_formula('rent ~ C(borough, Treatment("Manhattan"))', rentals).fit()
print(model.params)
Output:

Intercept                                         5138.940379
C(borough, Treatment("Manhattan"))[T.Brooklyn]   -1811.536627
C(borough, Treatment("Manhattan"))[T.Queens]     -2622.793057
dtype: float64
In this example, the reference category is 'Manhattan'. Therefore, the intercept is the mean rental price in Manhattan, and the other slopes are the mean differences for Brooklyn and Queens in comparison to Manhattan.

Other Python Libraries for fitting Linear Models
There are a few different Python libraries that can be used to fit linear regression models. It is therefore important to understand how this implementation differs for each library. In statsmodels, the creation of the X matrix happens completely “behind the scenes” once we pass in a model formula.

In scikit-learn (another popular library for linear regression), we actually need to construct the indicator variables ourselves. Note that we do not have to construct the extra column of 1s that we saw in the X matrix — this also happens behind the scenes in scikit-learn. In order to construct those indicator variables, the pandas get_dummies() function is extremely useful:

import pandas as pd
rentals = pd.get_dummies(rentals, columns = ['borough'], drop_first = True)
print(rentals.head())
Output:

    rent  borough_Manhattan  borough_Queens
0   5295                  0               0
1   4020                  1               0
2  16000                  1               0
3   3150                  0               1
4   2955                  0               1
Setting drop_first = True tells Python to drop the first indicator variable (for 'Brooklyn' in thie case), which is what we need for linear regression. We can then fit the exact same model using scikit-learn as follows:

from sklearn.linear_model import LinearRegression
 
X = rentals[['borough_Manhattan', 'borough_Queens']]
y = rentals[['rent']]
 
# Fit model
regr = LinearRegression()
regr.fit(X, y)
print(regr.intercept_)
print(regr.coef_)
LinearRegression()
[3327.40375123]
[[1811.5366274  -811.25642981]]
Conclusion
In this article, we’ve walked through an example of how to implement and interpret categorical predictors in a linear regression model. In the process, we’ve learned a little bit about what happens behind the scenes when we fit a linear model using statsmodels or scikit-learn. This knowledge will help prepare us to fit and interpret more complex models that build upon these foundations.

# [Linear Models in scikit-learn vs. statsmodels](https://www.codecademy.com/courses/linear-regression-mssp/articles/scikit-learn-vs-statsmodels-linear-regression)

Learn about the differences between scikit-learn and statsmodels with respect to linear regression in Python.

## Introduction

Statsmodels and scikit-learn are two commonly used packages for linear regression in Python. 
In this course, we have focused on implementation using statsmodels; 
however, it is useful to be able to fit models using multiple tools because each one provides functionality that may not be available in the other.

For context, statsmodels was built as an extension to the `scipy.stats` module so as to enable R-like functionality in Python to perform statistical model implementation, 
testing, and inference. 
Scikit-learn is built on NumPy and SciPy to enable easy implementation of machine learning algorithms. 
It also contains a suite of associated model validation methods to fine-tune a model.

## A Comparison

### statsmodels
* Pro: Provides comprehensive model summaries, including t-tests for all the coefficients, R-squared, adjusted R-squared, AIC, BIC, log likelihood, F-test, and more.
* Pro: Allows users to fit models using a formula-based syntax, which makes it relatively simple to test out interaction terms and polynomial terms, compare multiple models, etc
* Con: It is missing some useful functions to easily perform operations on statsmodels model objects (e.g., k-fold validation, train-test split, lasso regression).
* Con: It is used less widely than scikit-learn, so has less detailed documentation and example code available online.

### scikit-learn
* Pro: Contains many easy-to-use functions that can perform operations like k-fold validation, train-test split, etc. in a few lines of code.
* Pro: Great documentation online and a large community of people who have shared their code and asked/answered questions online.
* Con: The model object contains more limited information (just coefficients and R-squared).
* Con: To fit a model, scikit-learn requires users to create the design matrix “by-hand” (or using other libraries), 
which means it requires an extra step to fit models with categorical variables, interaction terms, and/or polynomial terms.

Overall, most people use scikit-learn when performing predictive modeling, but aren’t concerned with examining the coefficients or their associated statistics. 
Meanwhile, statsmodels is great for comparing and fitting complex models; 
however, in order to use scikit-learn’s tools like k-fold cross-validation, you may need to transform your statsmodels model object into a scikit-learn model object.

## Implementation

To compare these libraries, let’s fit some models with each and compare the results:

### statsmodels
All of these examples use a dataset of air quality measurements, which is available via statsmodels. 
The code below uses this data to fit a model to predict temperature (`Temp`) based on ozone levels (`Ozone`), windspeed (`Wind`) and an interaction between `Ozone` and `Wind`.
```py
# Load libraries
import statsmodels.api as sm
 
# Get some data
data = sm.datasets.get_rdataset('airquality').data
data.dropna(inplace = True)
 
# Fit model
model = sm.OLS.from_formula(
    'Temp ~ Ozone + Wind + Ozone:Wind', 
    data
).fit()
print(model.summary())
```
Output:
```py
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   Temp   R-squared:                       0.563
Model:                            OLS   Adj. R-squared:                  0.551
Method:                 Least Squares   F-statistic:                     46.00
Date:                Thu, 08 Apr 2021   Prob (F-statistic):           3.54e-19
Time:                        15:37:34   Log-Likelihood:                -361.26
No. Observations:                 111   AIC:                             730.5
Df Residuals:                     107   BIC:                             741.4
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     79.3074      3.288     24.123      0.000      72.790      85.825
Ozone          0.0202      0.046      0.443      0.659      -0.070       0.111
Wind          -1.0550      0.286     -3.695      0.000      -1.621      -0.489
Ozone:Wind     0.0234      0.006      4.070      0.000       0.012       0.035
==============================================================================
Omnibus:                        4.265   Durbin-Watson:                   1.169
Prob(Omnibus):                  0.119   Jarque-Bera (JB):                3.491
Skew:                          -0.326   Prob(JB):                        0.175
Kurtosis:                       2.426   Cond. No.                     2.22e+03
==============================================================================
```

### scikit-learn:

In scikit-learn, it is relatively easy to fit a model with any predictor set that already exists in our data. 
For example, we can fit a model to predict temperature based on ozone level (`Ozone`) and windspeed (`Wind`) as follows:
```py
from sklearn.linear_model import LinearRegression
 
X = data[['Ozone', 'Wind']]
y = data[['Temp']]
 
# Fit model
model = LinearRegression()
model.fit(X, y)
print(model.intercept_)
print(model.coef_)
```
Output:
```py
[73.14445315]
[[ 0.18059202 -0.29723628]]
```
However, if we want to add interaction terms, polynomial terms, or anything else more complex, we need to do that ahead of time. 
For example, if we want to add an interaction between `Ozone` and `Wind` like we did in statsmodels, we can create a new column in our dataset named `OzoneWind`, 
which is derived by multiplying `Ozone` and `Wind` together. 
Then, we can add that column to our model and produce the same coefficients as we calculated with statsmodels:
```py
data['OzoneWind'] = data.Ozone * data.Wind
X = data[['Ozone', 'Wind', 'OzoneWind']]
y = data[['Temp']]
 
# Fit model
model = LinearRegression()
model.fit(X, y)
print(model.intercept_)
print(model.coef_)
```
Output:
```py
[79.30741717]
[[ 0.02024914 -1.05495668  0.02342465]]
```
Alternatively, we could create the X matrix with formula notation via the `patsy` module. 
Note that we have to include a `0 +` in front of our formula
so that `patsy` doesn’t automatically generate a column of `1`s in the `X` matrix for the intercept (`sklearn.linear_model.LinearRegression` does this under the hood). 
The code to implement this is shown below:
```py
import patsy
 
# Fit model
y, X = patsy.dmatrices(
    'Temp ~ 0 + Ozone + Wind + Ozone:Wind', 
    data
)
model = LinearRegression() 
model.fit(X, y) 
print(model.intercept_)
print(model.coef_)
```
Output:
```py
[79.30741717]
[[ 0.02024914 -1.05495668  0.02342465]]
```
Note that we calculated the same intercept and coefficients using statsmodels and scikit-learn. While statsmodels gave us more information about the model and coefficients, 
there are some operations that are much simpler in scikit-learn. 
For example, the following lines of code will split our data into training and test sets. 
There is no function in statsmodels to easily do the same.
```py
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size = 0.25
)
```

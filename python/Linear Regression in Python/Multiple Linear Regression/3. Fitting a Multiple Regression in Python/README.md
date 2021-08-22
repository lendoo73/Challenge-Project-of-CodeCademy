#### MULTIPLE LINEAR REGRESSION

# [Fitting a Multiple Regression in Python](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/fitting-a-multiple-regression-in-python)

To run a multiple linear regression in Python, we can use the function `OLS.from_formula()` from `statsmodels.api`. 
For example, if we want to run a regression to predict `score` using `hours_studied` and `breakfast` (contained in a dataset named `survey`), we can fit the model as follows:
```py
import statsmodels.api as sm
model = sm.OLS.from_formula(
    'score ~ hours_studied + breakfast', 
    data = survey
).fit()
```
To actually view the results, we can print a summary of them to the console using the following code.
```py
print(model.summary())
```
Rather than printing the entire summary table, we can call the model coefficients directly using `nodel.params`. 
We can even call a specific coefficient by order of appearance in the table. For instance:
```py
print(model.params)
# Output:
# Intercept        32.665570
# hours_studied     8.540499
# breakfast        22.495615
 
print(model.params[0])
# Output:
# 32.66556979549575
```
From the coefficient table, we can see the intercept is approximately 32.7, the coefficient on `hours_studied` is 8.5, and the coefficient on `breakfast` is 22.5.

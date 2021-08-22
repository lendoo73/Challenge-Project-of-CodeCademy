#### MULTIPLE LINEAR REGRESSION

# [Changes in Predictor Coefficients](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/changes-in-predictor-coefficients)

Sometimes we use regression to understand the relationship between two variables because we wish to control for potential confounders. 
For example, based on the `survey` dataset, we may be primarily interested in how studying (`hours_studied`) is related to test score (`score`); 
however, in order to understand this relationship, we may want to control for additional student attributes, such as whether the student ate breakfast (`breakfast`).

If we perform a simple linear regression predicting `score` from `hours_studied`, we get the following results:
```py
import statsmodels.api as sm
model0 = sm.OLS.from_formula(
    'score ~ hours_studied', 
    data = survey
).fit()
print(model0.params)
 
# Output:
# Intercept        34.990700
# hours_studied    11.881045
```
However, if we add `breakfast` to the model and inspect the new coefficients, we’ll find that the intercept and slope on `hours_studied` have changed:
```py
import statsmodels.api as sm
model1 = sm.OLS.from_formula(
    'score ~ hours_studied + breakfast', 
    data = survey)
.fit()
print(model1.params)
 
# Output:
# Intercept        32.665570
# hours_studied     8.540499
# breakfast        22.495615
```
Note that the coefficient on `hours_studied` changes from 11.9 to 8.5. 
Why does this happen? 
Perhaps people who eat breakfast are more likely to study longer and also more likely to score better on their exam. 
Without taking `breakfast` into account, some of the relationship between `score` and `breakfast` is attributed to `hours_studied` instead.

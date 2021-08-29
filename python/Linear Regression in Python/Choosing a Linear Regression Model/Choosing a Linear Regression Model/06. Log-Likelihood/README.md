#### CHOOSING A LINEAR REGRESSION MODEL

# [Log-Likelihood](https://www.codecademy.com/courses/linear-regression-mssp/lessons/choosing-a-linear-regression-model/exercises/log-likelihood)

So far, we’ve used R-squared, adjusted R-squared, and an F-test to compare models. 
These criteria are most useful for finding a model that best fits an observed set of data. 
They are often used when our goal is interpreting a model to understand relationships between variables.

If our goal is to choose the best model for making predictions for new/unobserved data, we may want to use a likelihood based criteria instead.

Log-likelihood of a linear regression model essentially measures the probability of observing our data given a particular model. 
**Higher log-likelihood is better.**

For example, we can compare two models based on log likelihood as follows:
```py
model1 = sm.OLS.from_formula(
    'rent ~ bedrooms + size_sqft + min_to_subway', 
    data = rentals
).fit()
 
model2 = sm.OLS.from_formula(
    'rent ~ bathrooms + building_age_yrs + borough', 
    data = rentals
).fit()
 
print(model1.llf) #Output: -44282.327
print(model2.llf) #Output: -44740.623
```
Because model 1 has a higher log-likelihood (a smaller negative number is larger), we would choose model 1 over model 2.

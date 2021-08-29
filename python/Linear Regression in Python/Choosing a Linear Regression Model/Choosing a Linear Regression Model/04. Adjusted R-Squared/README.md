#### CHOOSING A LINEAR REGRESSION MODEL

# [Adjusted R-Squared](https://www.codecademy.com/courses/linear-regression-mssp/lessons/choosing-a-linear-regression-model/exercises/adjusted-r-squared)

While R-squared is useful for comparing models with different sets of predictors, we saw that it could lead to overfitting when choosing between nested models.

To address this issue, we can instead use ***adjusted R-squared***, which gives a small penalty for each additional predictor in a model. 
For example:
```py
model1 = sm.OLS.from_formula(
    'rent ~ bedrooms + size_sqft + borough', 
    data = rentals
).fit()
 
model2 = sm.OLS.from_formula(
    'rent ~ bedrooms + size_sqft + borough + has_doorman', 
    data = rentals
).fit()
 
print(model1.rsquared) #Output: 0.72761
print(model2.rsquared) #Output: 0.72765
 
print(model1.rsquared_adj) #Output: 0.72739
print(model2.rsquared_adj) #Output: 0.72738
```
Note that the second model (with an additional predictor) has a slightly larger R-squared, but a slightly smaller adjusted R-squared, compared to the first model. 
Based on the adjusted R-squared, we would choose the smaller model.

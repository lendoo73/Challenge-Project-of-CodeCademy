#### CHOOSING A LINEAR REGRESSION MODEL

# [AIC and BIC](https://www.codecademy.com/courses/linear-regression-mssp/lessons/choosing-a-linear-regression-model/exercises/aic-and-bic)

Similarly to R-squared, log-likelihood only increases as we add more predictors to a model. 
In the same way that adjusted R-squared penalizes R-squared for more predictors, there are criteria that penalize the log-likelihood for more predictors.

The two most commonly used are ***Akaike information criterion (AIC)*** and ***Bayesian information criterion (BIC)***. 
Both AIC and BIC use negative log-likelihood, so **we actually want the model with the LOWEST AIC or BIC**.

AIC and BIC are similar, but *BIC gives a bigger penalty* for each additional predictor, so it is used for finding the best “simple” model. 
This is useful because it makes the model more interpretable. 
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
 
print(model1.llf) #Output: -43756.418
print(model2.llf) #Output: -43756.017
 
print(model1.aic) #Output: 87522.837
print(model2.aic) #Output: 87524.034
 
print(model1.bic) #Output: 87555.423
print(model2.bic) #Output: 87563.137
```
We see that the log-likelihood for model 2 is slightly larger (better), but the AIC for model 2 is slightly larger (worse), and BIC even more so. 
Both AIC and BIC would lead us to choose model 1, whereas log-likelihood would lead us to choose model 2.

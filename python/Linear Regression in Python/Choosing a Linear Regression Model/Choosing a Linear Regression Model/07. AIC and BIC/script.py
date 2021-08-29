# Load libraries
import pandas as pd
import statsmodels.api as sm

# Import data
bikes = pd.read_csv('bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula(
  'cnt ~ temp + hum + windspeed + season + holiday + weekday', 
  data = bikes
).fit()

# Fit model2
model2 = sm.OLS.from_formula(
  'cnt ~ temp + hum + windspeed + season + holiday + weekday + atemp', 
  data = bikes
).fit()

# Print log likelihood for both models
print(model1.llf)
print(model2.llf)

# Which model based on log likelihood?
which_model_loglik = 2

# Print AIC for both models
print(model1.aic)
print(model2.aic)

# Which model based on AIC?
which_model_aic = 1

# Print BIC for both models
print(model1.bic)
print(model2.bic)

# Which model based on BIC?
which_model_bic = 1

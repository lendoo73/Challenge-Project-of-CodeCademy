# Load libraries
import pandas as pd
import statsmodels.api as sm

# Import data
bikes = pd.read_csv('bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula(
  "cnt ~ temp + hum + windspeed + season + holiday + weekday",
  data = bikes
).fit()

# Fit model2
model2 = sm.OLS.from_formula(
  "cnt ~ temp + hum + windspeed + season + holiday + weekday + atemp",
  data = bikes
).fit()

# Print R-squared for both models
print(model1.rsquared)
print(model2.rsquared)

# Print adjusted R-squared for both models
print(model1.rsquared_adj)
print(model2.rsquared_adj)

# Which model based on R-squared?
which_model_rsq = 2

# Which model based on adjusted R-squared?
which_model_adj_rsq = 1

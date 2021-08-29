# Load libraries
import pandas as pd
import statsmodels.api as sm

# Import data
bikes = pd.read_csv('bikes.csv')

# cnt - the number of bike rentals
# Fit model1
model1 = sm.OLS.from_formula(
  "cnt ~ temp + windspeed + holiday",
  data = bikes
).fit()
print(model1.params)

# Fit model2
model2 = sm.OLS.from_formula(
  "cnt ~ hum + season + weekday",
  data = bikes
).fit()
print(model2.params)

# Print R-squared for both models
print(model1.rsquared)
print(model2.rsquared)

# Choose a model
which_model = 1

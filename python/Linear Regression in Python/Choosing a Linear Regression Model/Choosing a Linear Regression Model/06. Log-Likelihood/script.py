# Load libraries
import pandas as pd
import statsmodels.api as sm

# Import data
bikes = pd.read_csv('bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula(
  "cnt ~ temp + windspeed + holiday",
  data = bikes
).fit()

# Fit model2
model2 = sm.OLS.from_formula(
  "cnt ~ hum + season + weekday",
  data = bikes
).fit()

# Print log likelihood for both models
print(model1.llf)
print(model2.llf)

# Which model based on log likelihood?
which_model = 1

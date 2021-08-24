import pandas as pd
import statsmodels.api as sm

plants = pd.read_csv('plants.csv')
model1 = sm.OLS.from_formula(
  'height ~ weight + species', 
  data = plants
).fit()

# Fit model2 regression here:
model2 = sm.OLS.from_formula(
  'height ~ weight + species + weight:species', 
  data = plants
).fit()

# Print model1 results here:
print(model1.params)
print()

# Print model2 results here:
print(model2.params)
print()

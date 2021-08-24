import pandas as pd
import numpy as np
import statsmodels.api as sm

plants = pd.read_csv('plants.csv')

# Fit regression here:
model = sm.OLS .from_formula(
  "dead ~ light + np.power(light, 2)",
  data = plants
).fit()

# Print coefficients here:
print(model.params)

# Compute and save numDead10 and numDead18:
numDead10 = model.params[0] + model.params[1] * 10 + model.params[2] * np.power(10, 2)

numDead18 = model.params[0] + model.params[1] * 18 + model.params[2] * np.power(18, 2)

# Print numDead10 and numDead18:
print(numDead10)
print(numDead18)


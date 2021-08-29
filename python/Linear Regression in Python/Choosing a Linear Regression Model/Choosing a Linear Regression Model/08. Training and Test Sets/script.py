# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Set seed (don't change this)
np.random.seed(123)

# Import data
bikes = pd.read_csv('bikes.csv')

# Split bikes data
indices = range(len(bikes))
s = int(0.8 * len(indices))
train_ind = np.random.choice(
  indices, 
  size = s, 
  replace = False
)
test_ind = list(set(indices) - set(train_ind))
bikes_train = bikes.iloc[train_ind]
bikes_test = bikes.iloc[test_ind]

# Fit model1
model1 = sm.OLS.from_formula(
  'cnt ~ temp + atemp + hum', 
  data = bikes_train
).fit()

# Fit model2
model2 = sm.OLS.from_formula(
  'cnt ~ season + windspeed + weekday', 
  data = bikes_train
).fit()

# Calculate predicted cnt based on model1
fitted1 = model1.predict(bikes_test)

# Calculate predicted cnt based on model2
fitted2 = model2.predict(bikes_test)

# Calculate PRMSE for model1
true = bikes_test.cnt
prmse1 = np.mean( ( true - fitted1 ) ** 2 ) ** 0.5

# Calculate PRMSE for model2
prmse2 = np.mean( ( true - fitted2 ) ** 2 ) ** 0.5

# Print PRMSE for both models
print(prmse1)
print(prmse2)

# Which model based on log likelihood?
which_model = 1

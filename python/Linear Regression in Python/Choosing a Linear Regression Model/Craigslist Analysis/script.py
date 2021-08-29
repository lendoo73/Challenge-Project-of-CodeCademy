# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Set seed
np.random.seed(1)

# Import data
housing = pd.read_csv('craigslist.csv')

# 1. Fit model1
model1 = sm.OLS.from_formula(
  "price ~ type + sqfeet + beds + baths",
  data = housing
).fit()


# 2. Fit model2
model2 = sm.OLS.from_formula(
  "price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed",
  data = housing
).fit()

# 3. Fit model3
model3 = sm.OLS.from_formula(
  "price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed + cats_allowed + dogs_allowed",
  data = housing
).fit()

# 4. Print R-squared for all models
print(model1.rsquared)
print(model2.rsquared)
print(model3.rsquared)

# 5. Print adjusted R-squared for all models
print(model1.rsquared_adj)
print(model2.rsquared_adj)
print(model3.rsquared_adj)

# 6. Run an F test comparing model2 and model3
from statsmodels.stats.anova import anova_lm

anova_results = anova_lm(model1, model2)
print(anova_results)

# 7. Print log likelihood for all models
print(model1.llf)
print(model2.llf)
print(model3.llf)

# 8. Print AIC for all models
print(model1.aic)
print(model2.aic)
print(model3.aic)

# 9. Print BIC for all models
print(model1.bic)
print(model2.bic)
print(model3.bic)

# Split housing data
indices = range(len(housing))
s = int(0.8 * len(indices))
train_ind = np.random.choice(
  indices, 
  size = s, 
  replace = False
)
test_ind = list(set(indices) - set(train_ind))
housing_train = housing.iloc[train_ind]
housing_test = housing.iloc[test_ind]

# 10.
# Fit model2 with training data
model2_train = sm.OLS.from_formula(
  "price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed",
  data = housing_train
).fit() 

# Fit model3 with training data
model3_train = sm.OLS.from_formula(
  "price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed + cats_allowed + dogs_allowed",
  data = housing_train
).fit()

# 11. Calculate predicted price based on model2
fitted_mod2 = model2_train.predict(housing_test)

# Calculate predicted price based on model3
fitted_mod3 = model3_train.predict(housing_test)

# 12. Calculate PRMSE for model2
true = housing_test.price
prmse2 = np.mean((true - fitted_mod2) ** 2) ** 0.5

# Calculate PRMSE for model3
prmse3 = np.mean((true - fitted_mod3) ** 2) ** 0.5

# Print PRMSE for both models
print(prmse2)
print(prmse3)

# 13.
model_2_Win = 0
model_3_Win = 0
for n in range(7):
  np.random.seed(n + 1)
  # Split housing data
  indices = range(len(housing))
  s = int(0.8 * len(indices))
  train_ind = np.random.choice(
    indices, 
    size = s, 
    replace = False
  )
  test_ind = list(set(indices) - set(train_ind))
  housing_train = housing.iloc[train_ind]
  housing_test = housing.iloc[test_ind]
  # Fit model2 with training data
  model2_train = sm.OLS.from_formula(
    "price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed",
    data = housing_train
  ).fit() 

  # Fit model3 with training data
  model3_train = sm.OLS.from_formula(
    "price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed + cats_allowed + dogs_allowed",
    data = housing_train
  ).fit()

  # 11. Calculate predicted price based on model2
  fitted_mod2 = model2_train.predict(housing_test)

  # Calculate predicted price based on model3
  fitted_mod3 = model3_train.predict(housing_test)

  # 12. Calculate PRMSE for model2
  true = housing_test.price
  prmse2 = np.mean((true - fitted_mod2) ** 2) ** 0.5

  # Calculate PRMSE for model3
  prmse3 = np.mean((true - fitted_mod3) ** 2) ** 0.5

  # Print PRMSE for both models
  if prmse3 < prmse2:
    model_3_Win += 1
  else:
    model_2_Win += 1

print("Model 2 win:", model_2_Win)
print("Model 3 win:", model_3_Win)

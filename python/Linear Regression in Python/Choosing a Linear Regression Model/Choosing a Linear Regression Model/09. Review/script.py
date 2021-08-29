# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

# Import data
rentals = pd.read_csv('rentals.csv')

# Explore and test out models below:
# 1. Fit a few different models:
model1 = sm.OLS.from_formula(
  "rent ~ bedrooms + bathrooms + size_sqft",
  data = rentals
).fit()
print("Model 1:")
print(model1.params)
print(" ---------------- ")

model2 = sm.OLS.from_formula(
  "rent ~ bedrooms + bathrooms + size_sqft + has_doorman + borough",
  data = rentals
).fit()
print("Model 2:")
print(model2.params)
print(" ---------------- ")


model3 = sm.OLS.from_formula(
  "rent ~ bedrooms + has_roofdeck + has_doorman + has_patio + has_gym",
  data = rentals
).fit()
print("Model 3:")
print(model3.params)
print(" ---------------- ")

# 2. Compare the models based on adjusted R-squared. Which would you choose?
print("Model 1 adjusted R-squared: ", round(model1.rsquared_adj, 3))
print("Model 2 adjusted R-squared: ", round(model2.rsquared_adj, 3))
print("Model 3 adjusted R-squared: ", round(model3.rsquared_adj, 3))
print()
print("Choose the model with the higher adjusted R-squared value: model2 - ", round(model2.rsquared_adj, 3))

# 3. Compare the models using an F-test. Which would you choose?
anova_results = anova_lm(model1, model2)
print(anova_results)
print("Because the P-value is near 0 (small than 0.05), has_doorman + borough predictors significantly improves the model.")

# 4. Compare the models using AIC/BIC. Which would you choose?
# We actually want the model with the LOWEST AIC or BIC.
print(model1.aic)
print(model2.aic)
print(model1.bic)
print(model2.bic)
print("Because both AIC and BIC values of model2 lower than model1, model2 is the better.")

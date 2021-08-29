# Load libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
import codecademylib3

# Import data
bikes = pd.read_csv('bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula(
  "cnt ~ temp + hum + windspeed",
  data = bikes
).fit()

# Fit model2
model2 = sm.OLS.from_formula(
  "cnt ~ temp + hum + windspeed + weekday + atemp",
  data = bikes
).fit()

# Run the F-test and print results
anova_results = anova_lm(model1, model2)
print(anova_results.round(2))

print("If the p-value is less than 0.05, then we believe that at least one of the additional predictors in model2 is significantly different from 0. Therefore, we reject the null hypothesis and choose the larger model (model2).")

# Which model is better?
which_model = 2

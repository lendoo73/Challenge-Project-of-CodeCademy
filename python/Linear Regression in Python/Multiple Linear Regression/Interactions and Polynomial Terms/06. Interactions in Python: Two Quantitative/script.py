import pandas as pd
import statsmodels.api as sm

plants = pd.read_csv('plants.csv')

# Save model3 here:
model3 = sm.OLS.from_formula(
  "growth ~ water + fertilizer + water:fertilizer",
  data = plants
).fit()

# Print model3 coefficients here:
print(model3.params)

# Save slopeDiff here:
slopeDiff = 0.774034

# Save intercept3 and slope3 here:
intercept3 = 5.904379 - 1.196669 * 3
slope3 = 1.860867 + 0.774034 * 3

# Save intercept5 and slope5 here:
intercept5 = 5.904379 - 1.196669 * 5
slope5 = 1.860867 + 0.774034 * 5

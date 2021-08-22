import pandas as pd
import statsmodels.api as sm

student = pd.read_csv('student.csv')

# Fit regression model here:
model1 = sm.OLS.from_formula(
  "port3 ~ math1 + address",
  data = student
).fit()




# Print intercept and coefficients here:
print(model1.params)

# Save intercept and coefficients here:
b0 = model1.params[0]
b1 = model1.params[2]
b2 = model1.params[1]

import pandas as pd
import statsmodels.api as sm

student = pd.read_csv('student.csv')

# Run regression with only math1 here:
simple = sm.OLS.from_formula(
  "port3 ~ math1",
  data  = student
).fit()

# Run regression with math1 and port1 here:
multiple = sm.OLS.from_formula(
  "port3 ~ math1 + port1",
  data  = student
).fit()

# Print the results of simple here:
print(simple.params)

# Print the results of multiple here:
print(multiple.params)




# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Calculate fitted values
fitted_values = results.predict(students)

# Calculate residuals
residuals = students.score - fitted_values

# Plot a histogram of the residuals here:
plt.hist(residuals)

plt.show()
plt.clf()

# Plot the residuals against the fitted vals here:
plt.scatter(fitted_values, residuals)

plt.show()

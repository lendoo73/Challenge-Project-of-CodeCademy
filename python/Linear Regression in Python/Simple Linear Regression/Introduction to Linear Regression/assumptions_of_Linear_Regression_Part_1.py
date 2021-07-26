# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Calculate `fitted_values` here:
fitted_values = results.predict(students)

# Calculate `residuals` here:
residuals = students.score - fitted_values

# Print the first 10 residuals here:
print(residuals.head(5))

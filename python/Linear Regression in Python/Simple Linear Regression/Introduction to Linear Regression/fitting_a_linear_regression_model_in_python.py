# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Create the model here:
model = sm.OLS.from_formula("score ~ hours_studied", data = students)

# Fit the model here:
results = model.fit()

# Print the coefficients here:
print(results.params)

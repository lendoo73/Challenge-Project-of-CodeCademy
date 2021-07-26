# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
website = pd.read_csv('website.csv')

# Print the first five rows
print(website.head())

# Create a scatter plot of time vs age
plt.scatter(website.age, website.time_seconds)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict time_seconds based on age
model = sm.OLS.from_formula("time_seconds ~ age", website)
results = model.fit()
print(results.params)

# Plot the scatter plot with the line on top
plt.scatter(website.age, website.time_seconds)
plt.plot(website.age, results.params[0] + results.params[1] * website.age)

# Show then clear plot
plt.show()
plt.clf()

# Calculate fitted values
fitted_values = results.predict(website)

# Calculate residuals
residuals = website.time_seconds - fitted_values

# Check normality assumption
plt.hist(residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Predict amount of time on website for 40 year old
pred40 = results.params[0] + results.params[1] * 40
print('predicted time on website for a 40 year old: ', pred40)

# Fit a linear regression to predict time_seconds based on web_browser
model = sm.OLS.from_formula("time_seconds ~ browser", website)
results = model.fit()
print(results.params)

# Calculate and print the group means (for comparison)
mean_time_chrome = np.mean(website.time_seconds[website.browser == 'Chrome'])
mean_time_safari = np.mean(website.time_seconds[website.browser == 'Safari'])
print('Mean time (Chrome): ', mean_time_chrome)
print('Mean time (Safari): ', mean_time_safari)
print('Mean time difference: ', mean_time_chrome - mean_time_safari)

# Load libraries
import pandas as pd
import statsmodels.api as sm

# Import data
bikes = pd.read_csv('bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula('cnt ~ temp + atemp + hum + windspeed + weathersit + season + mnth + workingday + holiday + weekday + temp:mnth + temp:windspeed + temp:hum', data=bikes).fit()

# Print model1 summary
print(model1.summary())

# Fit model2
model2 = sm.OLS.from_formula('cnt ~ atemp + windspeed + mnth + holiday', data=bikes).fit()

# Print model2 summary
print(model2.summary())

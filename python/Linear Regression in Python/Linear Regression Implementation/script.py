# Load libraries
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np

# Get some data
data = sm.datasets.get_rdataset('airquality').data
data.dropna(inplace=True)

# Fit model1 with sm
model1 = sm.OLS.from_formula(
  "Temp ~ Month + Day",
  data = data
).fit()
print(model1.params)

# Fit model1 with sklearn
X = data[["Month", "Day"]]
y = data[["Temp"]]

model1 = LinearRegression()
model1.fit(X, y)
print(model1.intercept_)
print(model1.coef_)

# Fit model2 with sm
model2 = sm.OLS.from_formula(
  "Temp ~ Month + Day + Month:Day + Ozone + np.power(Ozone,2)",
  data = data
).fit()
print(model2.params)

# Fit model2 with sklearn
data["MonthDay"] = data["Month"] * data["Day"]
data["OzoneSquared"] = data["Ozone"] * data["Ozone"]
X = data[["Month", "Day", "MonthDay", "Ozone", "OzoneSquared"]]
model1 = LinearRegression()
model1.fit(X, y)
print(model1.intercept_)
print(model1.coef_)

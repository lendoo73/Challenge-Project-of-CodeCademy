import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")
# 1. Use .head() to get a sense of how this DataFrame is structured:
#print(df.head())

# 2. Use the .groupby() method to get the mean of totalprod per year:
prod_per_year = df.groupby("year").totalprod.mean().reset_index()
#print(prod_per_year)

# 3. Create a variable called X that is the column of year:
X = prod_per_year.year
#print(X)
# we will need to reshape it to get it into the right format:
X = X.values.reshape(-1, 1)
print(X)

# 4. Create a variable called y that is the totalprod column:
y = prod_per_year.totalprod 
#print(y)

# 5. Using plt.scatter(), plot y vs X as a scatterplot:
plt.scatter(X, y)
# Display the plot:
#plt.show()

# 6. Create a linear regression model from scikit-learn:
regr = linear_model.LinearRegression()
# 7. Fit the model to the data:
regr.fit(X, y)
# 8.
#print(regr.coef_[0])
#print(regr.intercept_)
# 9. Create a list called y_predict that is the predictions your regr model would make on the X data:
y_predict = regr.predict(X)
# 10. Plot y_predict vs X as a line, on top of your scatterplot:
plt.plot(X, y_predict)
plt.show()

# 11. Let’s predict what the year 2050 may look like in terms of honey production:
# create a NumPy array called X_future that is the range from 2013 to 2050:
X_future = np.array(range(2013, 2051))
#print(X_future)
#print(len(X_future))
# we need to reshape it for scikit-learn:
X_future = X_future.reshape(-1, 1)
#print(X_future)

# 12.
future_predict = regr.predict(X_future)
#print(len(future_predict))

# 13. Plot future_predict vs X_future:
plt.plot(X_future, future_predict )
#plt.show()
# How much honey will be produced in the year 2050?
# get index for 2050:
index = list(X_future).index(2050)
#print(index)
#print(X_future[index])
# get data for 2050:
honey_produced_2050 = future_predict[index]
print(honey_produced_2050)

plt.hlines(y = honey_produced_2050, xmin = 1998, xmax = 2050, color = 'r', linestyle = '--', label = int(honey_produced_2050))
plt.legend()
plt.title("How much honey will be produced in the year 2050?")
plt.xlabel("Year")
plt.ylabel("Honey production")
plt.show()

import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

b, m = gradient_descent(X, y, 0.0001, 1000)

y_predictions = [val * m + b for val in X]

plt.plot(X, y, 'o')
#plot your line here:
plt.plot(X, y_predictions)
plt.show()

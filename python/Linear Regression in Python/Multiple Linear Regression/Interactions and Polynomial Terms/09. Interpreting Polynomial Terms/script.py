import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

plants = pd.read_csv('plants.csv')

simple = sm.OLS.from_formula('dead ~ light', data=plants).fit()
polynomial = sm.OLS.from_formula('dead ~ light + np.power(light,2)', data=plants).fit()

# Print simple coefficients here:
print(simple.params)

# Print polynomial coefficients here:
print(polynomial.params)

# Uncomment scatter plot here:
sns.lmplot(
  x = 'light', 
  y = 'dead', 
  ci = None, 
  data = plants
)
x = np.linspace(0, 20, 100)
y = polynomial.params[0] + polynomial.params[1] * x + polynomial.params[2] * np.power(x, 2)
# Add polynomial line here:
plt.plot(
  x,
  y,
  linestyle = "dashed",
  linewidth = 4,
  color = "black"
)

# Uncomment legend and display:
plt.legend(['Simple Model','Polynomial Model'])
plt.show()

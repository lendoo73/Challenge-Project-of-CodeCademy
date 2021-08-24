import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import codecademylib3

# https://www.kaggle.com/nehatiwari03/harry-potter-fanfiction-data
# https://www.fanfiction.net/book/Harry-Potter/
hp = pd.read_csv('hp.csv')

# Try a scatter plot of two quantitative variables
sns.lmplot(
  x = 'reviews', 
  y = 'follows', 
  data = hp
)
plt.show()

# Try the same plot colored by a binary variable
sns.lmplot(
  x = 'reviews', 
  y = 'follows', 
  hue = 'harry', 
  markers = ['o','x'], 
  fit_reg = False, 
  data = hp
)
plt.show()


# Try a model predicting a quantitative variable from two predictors
model0 = sm.OLS.from_formula(
  'follows ~ reviews + harry', 
  data = hp
).fit()
print(model0.params)



# Try the same model but with an interaction term
model1 = sm.OLS.from_formula(
  'follows ~ reviews + harry + reviews:harry', 
  data = hp
).fit()
print(model1.params)

sns.lmplot(
  x = 'follows', 
  y = 'favorites', 
  fit_reg = False, 
  data = hp
)
plt.show()


# Try a polynomial model
modelP = sm.OLS.from_formula(
  'favorites ~ follows + np.power(follows,3)', 
  data = hp
).fit()
print(modelP.params)

x = np.linspace(3, 40, 100)
y = modelP.params[0] + modelP.params[1] * x + modelP.params[2] * (x**3)
## Scatter plot
sns.lmplot(
  x = 'follows', 
  y = 'favorites', 
  fit_reg = False, 
  data = hp
)
## Add line
plt.plot(
  x,
  y,
  linewidth = 4,
  linestyle = 'dashed',
  color = 'black'
)
plt.show()



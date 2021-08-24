import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

plants = pd.read_csv('plants.csv')

# Fit regression model here:
model = sm.OLS.from_formula(
  "height ~ weight + species",
  data = plants
).fit()

# Print coefficients here:
print(model.params)

# Uncomment the scatter plot below:
sns.lmplot(
  x = 'weight', 
  y = 'height', 
  hue = 'species', 
  markers = ['o','x'], 
  fit_reg = False, 
  data = plants
)
plt.show()



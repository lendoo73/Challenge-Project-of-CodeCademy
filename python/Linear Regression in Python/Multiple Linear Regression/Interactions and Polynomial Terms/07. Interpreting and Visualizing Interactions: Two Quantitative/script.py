import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

plants = pd.read_csv('plants.csv')
model = sm.OLS.from_formula(
  'growth ~ water + fertilizer + water:fertilizer', 
  data = plants
).fit()

# Create scatter plot here:
sns.lmplot(
  y  = "growth",
  x = "water",
  hue = "fertilizer", 
  data = plants,
  fit_reg = False
)

# Uncomment regression lines here:
plt.plot(
  plants.water, 
  model.params[0] + model.params[1] * plants.water+ model.params[2] * 2 + model.params[3] * plants.water*2, 
  color = 'lavender', 
  linewidth = 3
)
plt.plot(
  plants.water, 
  model.params[0] + model.params[1] * plants.water+ model.params[2] * 4 + model.params[3] * plants.water * 4, 
  color = 'mediumpurple', 
  linewidth = 3, 
  label = 'fertilizer=4'
)
# Add third line here:
plt.plot(
  plants.water, 
  model.params[0] + model.params[1] * plants.water+ model.params[2] * 6 + model.params[3] * plants.water * 6, 
  color = 'purple', 
  linewidth = 3, 
  label = 'fertilizer=6'
)


# Uncomment legend and display code here:
#plt.legend(['fertilizer=2','fertilizer=4','fertilizer=6'])
plt.show()

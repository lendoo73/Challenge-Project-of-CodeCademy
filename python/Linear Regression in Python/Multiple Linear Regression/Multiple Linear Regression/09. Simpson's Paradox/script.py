import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

sat = pd.read_csv('sat.csv')
model0 = sm.OLS.from_formula('total ~ expend', data=sat).fit()

# Print simple regression coefficients:
print(model0.params)

# Run regression with takingR added:
model1 = sm.OLS.from_formula(
  'total ~ expend + takingR', 
  data=sat
).fit()

# Print multiple regression coefficients:
print(model1.params)


# Code for scatter plot:
sns.lmplot(x='expend', y='total', hue='takingR', palette='colorblind', ci=None, data=sat)
# Add regression line for model0 here:
plt.plot(
  sat.expend, 
  model0.params[0] + model0.params[1] * sat.expend, 
  color='black', 
  linewidth = 3, 
  label = 'Only Books'
)

plt.show()



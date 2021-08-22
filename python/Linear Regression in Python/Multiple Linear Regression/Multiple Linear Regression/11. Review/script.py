import codecademylib3
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

family = pd.read_csv('family.csv')

#create heat map here:
corr_grid = family.corr()
palette = sns.diverging_palette(220, 20, sep=40, as_cmap=True)
sns.heatmap(
  corr_grid, 
  xticklabels = corr_grid.columns,
  yticklabels = corr_grid.columns, 
  center = 0, 
  cmap = palette, 
  vmin = -1, 
  vmax = 1, 
  annot = True
)
plt.show()


#fit model and view summary here:
model = sm.OLS.from_formula(
  'income ~ food + housing + source', 
  data = family
)
results = model.fit()
print(results.summary())

#write out regression equation here:
print(results.params)
# income = -26.809578 + 29.703311 * source + 1.528273 * food + 3.189324 * housing

#interpret intercept here:
# When food and housing expenditures are zero pesos, the average income is -26.8 thousand pesos (or -26,800 pesos) for people whose income comes from entrepreneurial activities (source = 0 group).

#interpret the coefficient on source here:
# Holding all other variables constant, the average income for people who earn their income through wages/salaries is 29.7 thousand pesos (or 29,700 pesos) higher than that of people who earn their income through entrepreneurial activities. In other words, the intercept of the Wage/Salaries regression line is 29.7 higher than the intercept of the Entrepreneurial Activities regression line.

#interpret the coefficient on food here:
# Holding all other predictors constant, as food expenditure increases by 1000 pesos, expected income increases by about 1500 pesos.

#interpret the coefficient on housing here:
# Holding all other predictors constant, as housing expenditure increases by 1000 pesos, expected income increases by about 3200 pesos.

#plot regression lines on scatter plot here:
sns.lmplot(
  x = 'housing', 
  y = 'income', 
  hue = 'source', 
  data = family
)
plt.plot(
  family.housing, 
  results.params[0] + results.params[1] * 1 + results.params[3] * family.housing + results.params[2] * 10, 
  color = 'red',
  linewidth = 5, 
  label = 'food=10'
)
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*100, color='orange',linewidth=5, label='food=100')
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*200, color='yellow',linewidth=5, label='food=200')
plt.legend()
plt.show()

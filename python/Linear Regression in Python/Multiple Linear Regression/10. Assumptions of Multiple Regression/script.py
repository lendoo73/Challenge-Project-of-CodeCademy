import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

student = pd.read_csv('student.csv')

# Save correlations here:
corrs = student.corr()

# Plot heatmap here:
sns.heatmap(
  corrs,
  xticklabels = corrs.columns, 
  yticklabels = corrs.columns, 
  vmin = -1, 
  center = 0, 
  vmax = 1, 
  cmap = 'PuOr', 
  annot = True
)
plt.show()

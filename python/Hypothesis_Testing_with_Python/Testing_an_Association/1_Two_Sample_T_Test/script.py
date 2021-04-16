import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3
from scipy.stats import ttest_ind
data = pd.read_csv('version_time.csv')

#separate out times for  two versions
old = data.time_minutes[data.version=='old']
new = data.time_minutes[data.version=='new']

#run the t-test here:
pval = ttest_ind(old, new)[1]
print(pval)

#determine significance
print("If the p-value is less than 0.05, we can conclude there is a significant difference.")
significant = True 

#plot overlapping histograms
plt.hist(old, alpha=.8, label='old')
plt.hist(new, alpha=.8, label='new')
plt.legend()
plt.show()

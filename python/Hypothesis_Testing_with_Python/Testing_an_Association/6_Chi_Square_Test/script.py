import pandas as pd
from scipy.stats import chi2_contingency

# read in and print data
ants = pd.read_csv("ants_grade.csv")
print(ants.head())

# create contingency table
table = pd.crosstab(ants.Grade, ants.Ant)
print(table)

# run Chi-Square test and print p-value
pval = chi2_contingency(table)[1]
print(pval)

# determine significance
significant = False

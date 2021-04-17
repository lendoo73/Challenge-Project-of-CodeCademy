# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# load data
heart = pd.read_csv('heart_disease.csv')
# 1. Inspect the Data:
print(heart.head())

# 2. Predictors of Heart Disease:
sns.boxplot(
  x = heart.heart_disease,
  y = heart.thalach
).set_title("The highest heart rate during exercise test")
plt.show()
plt.clf()

# 3.
thalach_hd = heart.thalach[heart.heart_disease == "presence"]
thalach_no_hd = heart.thalach[heart.heart_disease == "absence"]
#print(thalach_hd)

# 4.
diff_mean_thalach = np.absolute(
  thalach_hd.mean() - thalach_no_hd.mean()
)
diff_median_thalach = np.absolute(
  thalach_hd.median() - thalach_no_hd.median()
)
print("Difference in mean:", diff_mean_thalach)
print("Difference in median:", diff_median_thalach)

# 5-6. 
from scipy.stats import ttest_ind

pval = ttest_ind(thalach_hd, thalach_no_hd)[1]
print("P-value of two-sample t-test: ", pval)
threshold = 0.05
print("There is a significant difference in average thalach for people with heart disease compared to people with no heart disease.", pval < threshold)

# 7. investigate at least one other quantitative variable:
# 2.:
sns.boxplot(
  x = heart.heart_disease,
  y = heart.trestbps
).set_title("Resting blood pressure in mm Hg")
plt.show()
plt.clf()

# 3.:
trestbps_hd = heart.trestbps[heart.heart_disease == "presence"]
trestbps_no_hd = heart.trestbps[heart.heart_disease == "absence"]

# 4.:
diff_mean_trestbps = np.absolute(
  trestbps_hd.mean() - trestbps_no_hd.mean()
)
diff_median_trestbps = np.absolute(
  trestbps_hd.median() - trestbps_no_hd.median()
)
print("Difference in mean:", diff_mean_trestbps)
print("Difference in median:", diff_median_trestbps)

# 5-6.:
pval = ttest_ind(trestbps_hd, trestbps_no_hd)[1]
print("P-value of two-sample t-test: ", pval)
print("There is a significant difference in average resting blood pressure for people with heart disease compared to people with no heart disease.", pval < threshold)

# Chest Pain and Max Heart Rate
# 8.: Investigate the relationship between thalach (maximum heart rate achieved during exercise) and the type of heart pain a person experiences.
sns.boxplot(
  x = heart.cp,
  y = heart.thalach
).set_title("Relationship between thalach and the type of heart pain")
plt.show()
plt.clf

# 9.:
type_of_chest_pain = heart.cp.unique()
def value_of_thalach(chest_pain):
  return  heart.thalach[heart.cp == chest_pain]

thalach_typical = value_of_thalach(type_of_chest_pain[0])
thalach_asymptom = value_of_thalach(type_of_chest_pain[1])
thalach_nonangin = value_of_thalach(type_of_chest_pain[2])
thalach_atypical = value_of_thalach(type_of_chest_pain[3])

# 10.:
from scipy.stats import f_oneway

pval = f_oneway(
  thalach_typical,
  thalach_asymptom,
  thalach_nonangin,
  thalach_atypical
)[1]
print("ANOVA P-value: ", pval)
print("There is at least one pair of chest pain categories for which people in those categories have significantly different thalach.", pval < threshold)

# 11. Run another hypothesis test to determine which of those pairs are significantly different:
# Tukey's Range Test
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey_results = pairwise_tukeyhsd(
  heart.thalach,
  heart.cp,
  threshold
)
print(tukey_results)

# Heart Disease and Chest Pain
# 12. Create a contingency table of 'cp' and 'heart_disease':
Xtab = pd.crosstab(
  heart.cp,
  heart.heart_disease
)
print(Xtab)

# 13. Run a hypothesis test -> Chi-Square Test
from scipy.stats import chi2_contingency
pval = chi2_contingency(Xtab)[1]
print("Chi-Square Test P-value: ", pval)
print("There is a significant association between chest pain type and whether or not someone is diagnosed with heart disease.", pval < threshold)

# 14. Further Exploration
types = ["quantitative variable", "binary categorical variable", "multi categorical variable"]
print(f"age: {types[0]}")
print(f"sex: {types[1]}")
print(f"trestbps: {types[0]}")
print(f"chol: {types[0]}")
print(f"cp: {types[2]}")
print(f"exang: {types[1]}")
print(f"fbs: {types[1]}")
print(f"thalach: {types[0]}")
print(f"heart_disease: {types[1]}")
print(f"\nWhich hypothesis test to use for each variable?")
print("""
Two Sample T-Tests (for an association between a quantitative variable and a binary categorical variable)
ANOVA and Tukey Tests (for an association between a quantitative variable and a non-binary categorical variable)
Chi-Square Tests (for an association between two categorical variables)
""")

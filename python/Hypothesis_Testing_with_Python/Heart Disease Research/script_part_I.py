# import libraries
import codecademylib3
import pandas as pd
import numpy as np
# 3., 9.:  Import the function from scipy.stats...
from scipy.stats import ttest_1samp, binom_test
#import scipy

#print(scipy.version.version) # version: 1.4.1

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
#print(yes_hd.columns)

# 1.: investigate cholesterol levels for patients with heart disease
print("Patients with heart disease:")
chol_hd = yes_hd.chol

# 2.: Calculate the mean cholesterol level for patients who were diagnosed with heart disease
mean_chol_hd = chol_hd.mean()
print("The mean cholesterol level in mg/dl: ", mean_chol_hd)
print("It is higher than 240 mg/dl.", mean_chol_hd > 240)

# 3-4.:
pval = ttest_1samp(
  chol_hd,           # sample_distribution
  240                   # expected_mean
  #alternative = "greater" # People with heart disease have an average cholesterol level that is greater than 240 mg/dl
  # ver 1.4.1 not support 'alternative' argument :(
)[1] / 2
print("P-value: ", pval)
print("Heart disease patients have an average cholesterol level significantly greater than 240 mg/dl.", pval < 0.05)

# 5.:
print("\nPatients without heart disease:")
col_no_hd = no_hd.chol
mean_col_no_hd= col_no_hd.mean()
print("The mean cholesterol level in mg/dl: ", mean_col_no_hd)
print("It is higher than 240 mg/dl.", mean_col_no_hd > 240)
pval = ttest_1samp(
  col_no_hd,
  240
)[1] / 2
print("P-value: ", pval)
print("Do patients without heart disease have average cholesterol levels significantly above 240 mg/dl?", pval < 0.05)

# 6. How many patients are there in this dataset? (heart)
num_patients = len(heart)
print("\nNumber of patients:", num_patients)

# 7. Calculate the number of patients with fasting blood sugar greater than 120:
num_highfbs_patients = len(heart[heart.fbs == 1])
print("Number of patients with fasting blood sugar greater than 120: ", num_highfbs_patients)

# 8.:
has_diabetes = round(num_patients * 0.08)
print("About 8% of the population has diabetes: ", has_diabetes)
print("Is this value similar to the number of patients with a resting blood sugar above 120 mg/dl — or different?", "Different: {num_highfbs_patients} > {has_diabetes}".format(
  num_highfbs_patients = num_highfbs_patients, 
  has_diabetes = has_diabetes
))

# 9.:
pval = binom_test(
  num_highfbs_patients, # # Number of patients with fasting blood sugar
  n = num_patients,         # the number of patients
  p = 0.08,                 # the expected probability of success
  alternative = "greater" 
)
print("\nP-value: ", pval)
print("This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl: ", pval < 0.05)



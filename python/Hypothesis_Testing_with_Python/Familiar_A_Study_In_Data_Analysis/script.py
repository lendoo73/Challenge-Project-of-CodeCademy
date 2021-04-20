# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# What Can Familiar Do For You?
# 1.:
print(lifespans.head())

# 2.:
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == "vein"]

# 3.:
print(vein_pack_lifespans.mean())

# 4.:
from scipy.stats import ttest_1samp

# 5.:
pval = ttest_1samp(vein_pack_lifespans, 73)[1]
threshold = 0.05
print(pval)
print("Is the average lifespan of a Vein Pack subscriber significantly longer than 73 years?", pval < threshold)

# Upselling Familiar: Pumping Life Into The Company
# 6.:
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == "artery"]

# 7. Calculate the average lifespan for Artery Pack subscribers:
print(artery_pack_lifespans.mean())
print("Is it longer than for the Vein Pack?", "False")

# 8.:
from scipy.stats import ttest_ind

pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)[1]
print(pval)
print("Is the average lifespan of a Vein Pack subscriber significantly different from the average lifespan of an Artery Pack subscriber?", pval < threshold)

# Side Effects: A Familiar Problem
# 10.:
print(iron.head())

# 11.:
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)

# 12.:
from scipy.stats import chi2_contingency

# 13.:
pval = chi2_contingency(Xtab)[1]
print(pval)
print("Is there a significant association between which pack (Vein vs. Artery) someone subscribes to and their iron level?", pval < threshold)

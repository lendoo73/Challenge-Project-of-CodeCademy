# Import libraries
import numpy as np
import pandas as pd
import codecademylib3

# Import data
dogs = pd.read_csv('dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

# 1.:
print(dogs.head())

# 2.:
whippet_rescue = dogs.is_rescue[dogs.breed == "whippet"]

# 3. How many whippets are rescues?:
num_whippet_rescues = whippet_rescue.sum()
print("How many whippets are rescues?", num_whippet_rescues )

# 4. How many whippets are in this sample of data in total?:
num_whippets = len(whippet_rescue)
print("How many whippets are in this sample of data in total?", num_whippets )

# 5.:
from scipy.stats import binom_test

p_value = binom_test(num_whippet_rescues, num_whippets, p = 0.08)
print(p_value)
threshold = 0.05
print("Is the proportion of whippets who are rescues significantly different from 8%?", p_value < threshold)

# 6. Is there a significant difference in the average weights of dog breeds?: 
wt_whippets = dogs.weight[dogs.breed == "whippet"]
wt_terriers = dogs.weight[dogs.breed == "terrier"]
wt_pitbulls = dogs.weight[dogs.breed == "pitbull"]

# 7.:
# ANOVA Test
from scipy.stats import f_oneway

pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)[1]
print(pval)
print("Is there at least one pair of dog breeds that have significantly different average weights?", pval < threshold)

# 8. Determine which of those breeds (whippets, terriers, and pitbulls) weigh different amounts on average.:
# Tukey’s Range Test
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey_results = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed, 0.05)
print(tukey_results)
print("Which of those breeds (whippets, terriers, and pitbulls) weigh different amounts on average?")
print("pitbull vs. terrier and terrier vs. whippet")

# 9. Is poodlies and shihtzus come in different colors?
Xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print(Xtab)

# 10.:
from scipy.stats import chi2_contingency
pval = chi2_contingency(Xtab)[1]
print(pval)
print("Do poodles and shihtzus come in significantly different color combinations?", pval < threshold)

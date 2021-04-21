# Import libraries
import codecademylib3
import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

# 1. Inspect the data:
print(abdata.head())

# 2. create a contingency table:
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)
print("Which group appears to have the highest number of purchases?", f"Group A has the highest number of purchases, with {Xtab.Yes.max()} purchases.")

# 3.:
from scipy.stats import chi2_contingency

pval = chi2_contingency(Xtab)[1]
print(pval)
threshold = 0.05
print("is there a significant difference in the purchase rate for groups A, B, and C?", pval < threshold)

# 4. Calculate the number of visitors:
num_visits = len(abdata)
print(num_visits)
num_visits = abdata.user_id.nunique()
print(num_visits)

# 5. calculate the number of visitors who would need to purchase the upgrade package at each price point ($0.99, $1.99, $4.99):
num_sales_needed_099 = 1000 / 0.99
print(num_sales_needed_099)

# 6. calculate the proportion of weekly visitors who would need to make a purchase in order to meet that goal:
p_sales_needed_099 = num_sales_needed_099 / num_visits
print(p_sales_needed_099)

# 7. ... for the other price points ($1.99 and $4.99):
num_sales_needed_199 = 1000 / 1.99
num_sales_needed_499 = 1000 / 4.99
p_sales_needed_199 = num_sales_needed_199 / num_visits
p_sales_needed_499 = num_sales_needed_499 / num_visits

print(p_sales_needed_199)
print(p_sales_needed_499)

# 8. :
# The number of visitors in group A:
samp_size_099 = len(abdata[abdata.group == "A"])
# The number of visitors in Group A who made a purchase:
sales_099 = len(abdata[
  (abdata.group == "A") & 
  (abdata.is_purchase == "Yes")
])
print(samp_size_099)
print(sales_099)

# 9. Calculate the sample size and number of purchases in group B (the $1.99 price point) and group C (the $4.99 price point):
samp_size_199 = len(abdata[abdata.group == "B"])
sales_199 = len(abdata[
  (abdata.group == "B") & 
  (abdata.is_purchase == "Yes")
])
print(samp_size_199)
print(sales_199)

samp_size_499 = len(abdata[abdata.group == "C"])
sales_499 = len(abdata[
  (abdata.group == "C") & 
  (abdata.is_purchase == "Yes")
])
print(samp_size_499)
print(sales_499)

# 10. For Group A ($0.99 price point), perform a binomial test
from scipy.stats import binom_test

pvalueA = binom_test(
  sales_099,     # the number of purchases
  samp_size_099, # the total number of visitors
  p = p_sales_needed_099, # the target percent of purchases
  alternative = "greater"
)
print("P-value A: ", pvalueA)

# 11. ...For Group B:
pvalueB = binom_test(
  sales_199,
  samp_size_199,
  p = p_sales_needed_199,
  alternative = "greater"
)
print("P-value B:", pvalueB)

# 12. ...For Group C:
pvalueC = binom_test(
  sales_499,
  samp_size_499,
  p = p_sales_needed_499,
  alternative = "greater"
)
print("P-value C:", pvalueC)

# 13. where the purchase rate was significantly higher than the target?
print("What price should Brian charge for the upgrade package?", "recommended price: $4.99")


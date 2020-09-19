import codecademylib
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import binom_test

df = pd.read_csv("clicks.csv")
print(df.head())

df['is_purchase'] = df.click_day.apply(
  lambda day: "Purchase" if pd.notnull(day) else "No Purchase"
)
#print(df)

purchase_counts = df.groupby(["group", "is_purchase"]).user_id.count().reset_index()
print(purchase_counts)

contingency = [
  [316, 1350],
  [183, 1483],
  [83, 1583]
]

pvalue = chi2_contingency(contingency)[1]
print(pvalue)

is_significant = True if pvalue < 0.05 else False

print(is_significant)
print("There is a significant difference between the three groups")

num_visits = len(df)

p_clicks_099 = 1000 / 0.99 / num_visits
p_clicks_199 = 1000 / 1.99 / num_visits
p_clicks_499 = 1000 / 4.99 / num_visits
print(p_clicks_099)
print(p_clicks_199)
print(p_clicks_499)

p_clicks_099 = (1000 / 0.99) / num_visits
p_clicks_199 = (1000 / 1.99) / num_visits
p_clicks_499 = (1000 / 4.99) / num_visits
# x: The number of successes
# n: The number of trials
# p: The hypothesized probability of success. 0 <= p <= 1. The default value is p = 0.5.
#  binom_test(x, n, p)
pvalueA = binom_test(316, 1350 + 316, p_clicks_099)
print(pvalueA)
pvalueB = binom_test(183, 183 + 1483, p_clicks_199)
print(pvalueB)
pvalueC = binom_test(83, 83 + 1583, p_clicks_499)
print(pvalueC)

final_answer = 4.99

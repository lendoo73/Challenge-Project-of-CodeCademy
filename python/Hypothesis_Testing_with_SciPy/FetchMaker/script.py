import numpy as np
# 1:
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

# 2:
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
#print(rottweiler_tl)
# 3:
#print(np.mean(rottweiler_tl))
#print(np.std(rottweiler_tl))
# 4:
whippet_rescue = fetchmaker.get_is_rescue("whippet")
#print(whippet_rescue)
# 5.
num_whippet_rescues = np.count_nonzero(whippet_rescue)
#num_whippet_rescues = whippet_rescue[whippet_rescue == 1]
#print(num_whippet_rescues)
# 6:
num_whippets = np.size(whippet_rescue)
#print(num_whippets)
# 7:
'''
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom_test.html
binom_test(
  x: The number of successes,
  n: The number of trials,
  p: The hypothesized probability of success.
)
'''
whippet_rescue_binom_test = binom_test(num_whippet_rescues, num_whippets, 0.08)
#8:
#print(whippet_rescue_binom_test)
#print("Not significant.")
# 9:
# ANOVA
# The one-way ANOVA tests the null hypothesis that two or more groups have the same population mean. The test is applied to samples from two or more groups, possibly with differing sizes.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html
whippets_weight = fetchmaker.get_weight("whippet")
terriers_weight = fetchmaker.get_weight("terrier")
pitbulls_weight = fetchmaker.get_weight("pitbull")
#print(np.mean(whippets_weight))
#print(np.mean(terriers_weight))
#print(np.mean(pitbulls_weight))
stat, pvalue = f_oneway(whippets_weight, terriers_weight, pitbulls_weight)
#print(pvalue)
#print("There is significant different the weight any of the above breeds.")
# 10:
'''
https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html

Tukey's Range Test:
pairwise_tukeyhsd(
  endog: values -> whippets_weight, terriers_weight and pitbulls_weight, 
  groups: labels, 
  alpha=0.05: pvalue)
'''
values = np.concatenate([whippets_weight, terriers_weight, pitbulls_weight])
labels = ["whippet"] * len(whippets_weight) + ["terrier"] * len(terriers_weight) + ["pitbull"] * len(pitbulls_weight)
tukeys_range_test = pairwise_tukeyhsd(values, labels, 0.05)
#print(tukeys_range_test)
#print("Where the reject value is True (pvalue is less than 0.05) between the dog breeds has significant different weight.")
# 11:
poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")
# 12:
#print(set(poodle_colors))
#print(set(shihtzu_colors))
colors = {}
for color in set(shihtzu_colors):
  colors[color] = [np.count_nonzero(poodle_colors == color), np.count_nonzero(shihtzu_colors == color)]
color_table = [colors["black"], colors["brown"], colors["gold"], colors["grey"], colors["white"]]
#print(color_table)
# 13:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html
chi2_test_result = chi2_contingency(color_table)
print("The p-value is: {}".format(chi2_test_result[1]))
print("The p-value is less than 0.05, so there is significant differnt between the poodle's colors and shihtzu's colors.")

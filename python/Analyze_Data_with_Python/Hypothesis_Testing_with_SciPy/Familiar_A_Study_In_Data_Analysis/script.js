# 1:
import familiar
# 3:
from scipy.stats import ttest_1samp
# 8:
from scipy.stats import ttest_ind
# 14:
from scipy.stats import chi2_contingency

# 2:
vein_pack_lifespans = familiar.lifespans(package = "vein")
#print(vein_pack_lifespans)
# 4:
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
# 5:
#print("Is the results are significant?")
#print(vein_pack_test.pvalue < 0.05)
# 6:
if vein_pack_test.pvalue < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")
# 7:
artery_pack_lifespans = familiar.lifespans("artery")
#print(artery_pack_lifespans)
# 9:
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
#print(package_comparison_results.pvalue)
# 10:
if package_comparison_results.pvalue <= 0.05:
  print("the Artery Package guarantees even stronger results!")
else:
  print("the Artery Package is also a great product!")
  print("Since the p-value was greater than 0.05, we can't say that there is a significant difference between the life expectancy of the two packages.")
# 13:
iron_contingency_table = familiar.iron_counts_for_package()
#print(iron_contingency_table)
# 15:
iron_contingency_result = chi2_contingency(iron_contingency_table)
test_statistic = iron_contingency_result[0]
iron_pvalue = iron_contingency_result[1]
number_of_degrees_of_freedom = iron_contingency_result[2]
expected_frequencies = iron_contingency_result[3]
#print(iron_pvalue)
# 16:
if iron_pvalue <= 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")

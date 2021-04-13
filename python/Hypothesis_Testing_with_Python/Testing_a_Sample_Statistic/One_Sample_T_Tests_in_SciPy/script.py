from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

day_1 = daily_prices[0]
#print(day_1)

tstat, pval = ttest_1samp(day_1, 1000)
print(pval)

p_values = [ttest_1samp(day, 1000)[1] for day in daily_prices]
print(p_values[:10])
print(f"The smallest p-value is: {min(p_values)}.")

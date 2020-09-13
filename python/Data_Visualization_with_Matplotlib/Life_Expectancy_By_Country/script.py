import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
# 1:
#print(data.head())
#print(data.tail())
# 2:
life_expectancy = data["Life Expectancy"]
#print(life_expectancy)
# 3:
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
#print(life_expectancy_quartiles)
# 4:
plt.hist(life_expectancy)
# 5:
plt.axvline(70, color = "red", linestyle = "--", label = "70 year")
q = 0
for line in life_expectancy_quartiles:
  q += 1
  plt.axvline(line, linestyle = "--", color = "yellow")
  plt.text(line - 1, -5, 'Q{}'.format(q))
plt.legend()
plt.show()
# 6:
gdp = data["GDP"]
#print(gdp)
# 7:
median_gdp = np.median(gdp)
#print(median_gdp)
#print(np.quantile(gdp, 0.5))
# 8:
low_gdp = data[data["GDP"] <= median_gdp]
#print(low_gdp)
high_gdp = data[data["GDP"] > median_gdp]
#print(high_gdp)
# 9:
def get_quartiles(df):
  return np.quantile(df, [0.25, 0.5, 0.75])

low_gdp_quartiles = get_quartiles(low_gdp["Life Expectancy"])
#print(low_gdp_quartiles)
# 10:
high_gdp_quartiles = get_quartiles(high_gdp["Life Expectancy"])
#print(high_gdp_quartiles)
# 11:
def add_quartiles(df, color = "yellow"):
  quartiles = get_quartiles(df)
  q = 0
  for line in quartiles:
    q += 1
    plt.axvline(line, linestyle = "--", color = color)
    plt.text(line, -5, 'Q{}'.format(q))

plt.close("all")
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.xlabel("Year")
plt.ylabel("GDP")
plt.axvline(70, color = "red", linestyle = "--", label = "70 year")
add_quartiles(low_gdp["Life Expectancy"])
add_quartiles(high_gdp["Life Expectancy"], "blue")
plt.show()

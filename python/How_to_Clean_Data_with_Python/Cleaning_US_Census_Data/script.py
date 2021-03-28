import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob   # 2.

# ------- Inspect the Data! -------
# 2.:
files = glob.glob("states*.csv")
us_census_list = [pd.read_csv(filename) for filename in files]

us_census = pd.concat(us_census_list)

#print(us_census.info())
#print(us_census.describe())
# 3.:
#print(us_census.columns)
#print(us_census.dtypes)

# 4.:
#print(us_census.head())

# ------- Regex to the Rescue -------
# 5. Splitting by Index:
us_census.Income = pd.to_numeric(us_census.Income.str[1:])
#print(us_census.head())
#print(us_census.dtypes)

# 6-7. Splitting by Character:
genders = us_census.GenderPop.str.split("_")
#print(genders)
us_census["Men"] = pd.to_numeric(genders.str.get(0).str[:-1])
us_census["Women"] = pd.to_numeric(genders.str.get(1).str[:-1])
#print(us_census.head())
#print(us_census.dtypes)

# 8.:
#plt.scatter(us_census.Women, us_census.Income)
#plt.show()
#plt.clf()

# 9. Fill the missing values:
us_census = us_census.fillna(
  value = {
    "Women": us_census.TotalPop - us_census.Men
  }
)
#print(us_census.head())
#print(us_census[["State", "Women"]])

# 10-11. Dealing with Duplicates:
#print(us_census.head(20))
#print(us_census.duplicated())
us_census = us_census.drop(columns = ["Unnamed: 0"])
us_census = us_census.drop_duplicates().reset_index(drop = True)
#print(us_census)
#print(us_census.duplicated())

# 12.:
plt.scatter(us_census.Women, us_census.Income)
plt.title("The Income of Womens")
plt.xlabel("Population of Women (millions)")
plt.ylabel("Income ($)")
x = [0, 5 * 10**6,10 * 10**6, 15 * 10**6, 20 * 10**6]
labels = [0, 5, 10, 15, 20]
plt.xticks(x, labels)
plt.show()
plt.clf()
#print(us_census[["Income", "Women"]])

# 13.:
#print(us_census.head())
#print(us_census.dtypes)
race_types = [
  "Hispanic",
  "White",
  "Black",
  "Native",
  "Asian",
  "Pacific"
]
races = us_census[race_types]
# Remove '%' useing Splitting by Index:
for column in races.columns:
  races[column] = pd.to_numeric(races[column].str[:-1])
print(races.head(6))
#print(races.dtypes)
#print(races.isna().sum())

# Fill the missing values:
races = races.fillna(
  value = {
    "Pacific": 100 - races.Hispanic - races.White - races.Black - races.Native - races.Asian
  }
)
#print(races.head(6))
#print(races.duplicated().sum())
print(us_census)
plt.figure(figsize = [15, 15])
for index, race in enumerate(races.columns):
  ax = plt.subplot(3, 2, index + 1)
  plt.hist(races[race])
  plt.title(race)

plt.suptitle("US Races", fontsize = 20)
plt.tight_layout(
  pad = 6
)
plt.show()
plt.clf()

# 15. US Races:
races["TotalPop"] = us_census.TotalPop
for race in races.columns[:-1]:
  races[f"{race}_pop"] = (races.TotalPop * races[race] / 100).round()

print(races.head())
# create barplot for each race:
sum_of_races = [ races[f"{race}_pop"].sum() for race in races if race in race_types]
print(sum_of_races)
plt.pie(
  sum_of_races,
  autopct = "%.1f%%",
  labels = race_types
)
plt.axis("equal")
plt.title("Races distribution in the United States", fontsize = 20)
plt.show()
plt.clf()

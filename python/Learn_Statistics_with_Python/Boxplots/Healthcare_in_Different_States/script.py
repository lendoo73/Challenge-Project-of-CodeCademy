import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
# 1. look at what data we have:
#print(healthcare.head())
#print(healthcare.columns)

# 2. see all of the different diagnoses:
print(healthcare["DRG Definition"].unique())

# 3. grab only the rows in the dataset that are about chest pain:
chest_pain = "313 - CHEST PAIN"
alcohol = "897 - ALCOHOL/DRUG ABUSE OR DEPENDENCE W/O REHABILITATION THERAPY W/O MCC"
chest_pain = healthcare[healthcare["DRG Definition"] == alcohol]
#print(chest_pain.columns)

# Separating By State:
# 4. get every chest pain diagnosis in Alabama:
alabama_chest_pain = chest_pain[chest_pain["Provider State"] == "AL"]
#print(alabama_chest_pain)

# 5. We now want to find the average cost of those diagnoses:
costs = alabama_chest_pain[" Average Covered Charges "].values
#print(costs)

# 6.  make a boxplot of those values:
#plt.boxplot(costs)
#plt.show()

# Making a Boxplot for All States:
# 7. we first need to create a list of all the states in our dataset:
states = chest_pain["Provider State"].unique()
#print(states)

# 8. separate the dataset into a dataset for each state:
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain["Provider State"] == state][" Average Covered Charges "].values)
#print(len(datasets))

# 9-10. draw 51 boxplots:
plt.figure(figsize = (20, 6))
plt.boxplot(
  datasets,
  labels = states
)
plt.show()


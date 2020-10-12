# 1. Import the modules:
#import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# 2-3. Load WorldCupMatches.csv into a DataFrame:
df = pd.read_csv("WorldCupMatches.csv")
# 4. Inspect the DataFrame:
print(df.head())

# 5. Create a new column in df named Total Goals, and set it equal to the sum of the columns Home Team Goals and Away Team Goals:
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]
print(df)

# 6. How many goals were scored each year the World Cup was held between 1930-2014?

# Setting styles:
sns.set_style("whitegrid")

# 7. To make the text in your visualization bigger and easier to read, set the context to be "poster":
sns.set_context("poster", font_scale = 0.8)

# 8. Create a figure and axes for your plot:
plt.subplots(figsize = (12, 7))

# 9. Visualize the columns Year and Total Goals as a bar chart:
ax = sns.barplot(
  data = df,
  x = "Year",
  y = "Total Goals",
  estimator = sum
)

goals_each_years = df.groupby("Year")["Total Goals"].sum().reset_index()
print(goals_each_years)

# 11. Give your bar chart a meaningful title:
#plt.title("Goals were scored each year")
ax.set_title("Goals were scored each year")

# rotating axis tick labels: 
# https://www.drawingfromdata.com/how-to-rotate-axis-labels-in-seaborn-and-matplotlib
ax.set_xticklabels(
  ax.get_xticklabels(), 
  rotation = 45
)

# 10. Render your bar chart:
plt.show()

# ---------------------------------------------
# 12. Load goals.csv into a DataFrame:
df_goals = pd.read_csv("goals.csv")
print(df_goals)

# 13. Setting the context of the plot:
sns.set_context("notebook", font_scale = 1.25)

# 14. Create a figure for your second plot:6
plt.subplots(figsize = (12, 7))

# 15. Set ax2 equal to a box plot:
ax2 = sns.boxplot(
  data = df_goals,
  x = "year",
  y = "goals",
  palette = "Spectral"
)
# 16. Give your box plot a meaningful and clear title:
plt.title("Averages goals per year in World Cup (1930 - 2014)")
ax2.set_xticklabels(
  ax2.get_xticklabels(), 
  rotation = 45
)

# 17. Render your box plot:
plt.show()


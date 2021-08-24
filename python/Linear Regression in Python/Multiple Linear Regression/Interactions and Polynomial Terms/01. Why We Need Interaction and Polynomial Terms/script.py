import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

plants = pd.read_csv('plants.csv')

# Scatter plot of height and weight here:
sns.lmplot(
  data  = plants,
  x = "weight",
  y = "height",
  hue = "species",
  fit_reg  = False
)
plt.show()

# Scatter plot of dead and light here:
sns.lmplot(
  data  = plants,
  x = "light",
  y = "dead",
  fit_reg  = False
)

plt.show()


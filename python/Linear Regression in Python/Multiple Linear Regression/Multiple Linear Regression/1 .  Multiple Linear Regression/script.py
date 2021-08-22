import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

student = pd.read_csv('student.csv')
print(student.head())

# Add code for scatter plot here:
sns.lmplot(
  x = "math1",
  y = "port3",
  hue = "address",
  data = student
)
plt.show()

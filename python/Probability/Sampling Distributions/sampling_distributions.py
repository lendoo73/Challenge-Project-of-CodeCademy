import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import codecademylib3

population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = population['Cod_Weight']

sample_size = 50
sample_means = []

for i in range(500):
  samp = np.random.choice(population, sample_size, replace = False)
  # calculate mean here
  this_sample_mean = np.mean(samp)
  # append here
  sample_means.append(this_sample_mean)

sns.histplot(sample_means,stat='density')
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

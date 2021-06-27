import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import codecademylib3

cod_population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = cod_population['Cod_Weight']

## Checkpoint 1:
sns.histplot(population, stat = 'density' )
plt.title("Population Distribution")
plt.show()

sample_means = []

# Below is our sample size
samp_size = 50

for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

## Checkpoint 2
plt.clf() # this closes the previous plot
sns.histplot(sample_means, stat = 'density' )
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

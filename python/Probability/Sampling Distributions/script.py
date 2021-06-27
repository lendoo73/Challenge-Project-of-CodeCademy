import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import codecademylib3

# Set up parameters here:
x = 0.24
population_mean = 0.25
population_std_dev = 0.2
samp_size = 10

### Below is code to create simulated dataset and calculate Standard Error
standard_error = population_std_dev / (samp_size**.5)

this_cdf = round(stats.norm.cdf(x,population_mean,standard_error),3)

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

# Simulate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)
std_sampling_distribution = round(np.std(sample_means),3)

std_error = population_std_dev / (samp_size **0.5)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} \n Population Std Dev: {population_std_dev} \n Standard Error = {population_std_dev} / sq rt({samp_size}) \n Standard Error = {std_error} ")
plt.xlabel("")
plt.show()
plt.clf()

# Plot the sampling distribution
sns.histplot(sample_means, stat = 'density')
plt.axvline(x,color='r',linestyle='dashed')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution} \n Sampling Dist Standard Deviation: {std_sampling_distribution}\n CDF for x={x}: {this_cdf}")
plt.xlabel("")
plt.show()

from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

# task 1: load in the spotify dataset
spotify_data = pd.read_csv("spotify_data.csv")

# task 2: preview the dataset
print(spotify_data.head())

# task 3: select the relevant column
song_tempos = spotify_data["tempo"]

# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)

# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")
print("The sample mean is an unbiased estimator of the population.")

# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")

# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")
print("The sample variance is a biased estimator of the population.")
print("The sample variance with the parameter 'ddof=1' is an unbiased estimator of the population.")
# task 13: calculate the population mean and standard deviation
population_mean = song_tempos.mean()
population_std = song_tempos.std()

# task 14: calculate the standard error
sampling_standard_deviation = population_std / (30 ** 0.5)

# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
probability = stats.norm.cdf(140, population_mean, sampling_standard_deviation)
print("The probability of the sample mean of 30 selected songs is less than 140bpm: ")
print(f"{round(probability * 100, 2)}%")

# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
probability = 1 - stats.norm.cdf(150, population_mean, sampling_standard_deviation)
print("The probability of the sample mean of 30 selected songs is greater than 150bpm: ")
print(f"{round(probability * 100, 2)}%")

# EXTRA


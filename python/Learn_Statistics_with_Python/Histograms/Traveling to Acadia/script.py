# import codecademylib3
#import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)

plt.subplot(2, 1, 1)
plt.hist(
  flights,
  range = (0, 365),
  bins = 365
)
plt.title("Flights by Day")
plt.xlabel("Day of the Year")
plt.ylabel("Flight Count")

plt.subplot(2, 1, 2)
plt.hist(
  in_bloom,
  range = (0, 365),
  bins = 365
)
plt.title("Blooms  by Day")
plt.xlabel("Day of the Year")
plt.ylabel("number of flowers")

plt.tight_layout()
plt.show()
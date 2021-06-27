import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## Setting up our parameters
std_dev = 20
samp_size = 25
standard_error = std_dev / (samp_size ** 0.5)

cod_cdf = stats.norm.cdf(30, 36, standard_error)
print(cod_cdf)

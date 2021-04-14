import numpy as np
import pandas as pd
from scipy.stats import binom_test

# calculate p_value_2sided here:
p_value_2sided = binom_test(
  41,     # the number of observed successes
  n = 500, # the number of total trials
  p = 0.1  # the expected probability of success
)
print(p_value_2sided)
print(f"IF the true probability of purchasing is 0.1, the probability of observing 41 or fewer purchasing OR 59 or more purchasing is {p_value_2sided} ({(p_value_2sided * 100):.2f}%)")
print()
# calculate p_value_1sided here:
p_value_1sided = binom_test(
  41,
  n = 500,
  p = 0.1,
  alternative = "less"
)
print(p_value_1sided)
print(f"IF the true probability of purchasing is 0.1, the probability of observing 41 or fewer purchasing is {p_value_1sided} ({(p_value_1sided * 100):.2f}%)")

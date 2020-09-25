from math import log, sqrt

def display_as_percentage(val):
  return "{:.1f}%".format(val * 100)

def calculate_simple_return(start_price, end_price, dividend = 0):
  return (end_price - start_price + dividend) / start_price

def calculate_log_return(start_price, end_price):
  return log(end_price / start_price)

def annualize_return(log_return, t):
  return log_return * t

def convert_returns(log_returns, t):
  return sum(log_returns) / len(log_returns) * t

def calculate_variance(dataset):
  mean = sum(dataset) / len(dataset)
  numerator = 0
  for data in dataset:
    numerator += (data - mean) ** 2
  return numerator / len(dataset)

def calculate_stddev(dataset):
  variance = calculate_variance(dataset)
  stddev = sqrt(variance)
  return stddev

def calculate_correlation(set_x, set_y):
  # Sum of all values in each dataset
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  # Sum of all squared values in each dataset
  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y ** 2 for y in set_y])

  sum_xy = sum([x * y for x, y in zip(set_x, set_y)])
  # Length of dataset
  n = len(set_x)

  # Calculate correlation coefficient
  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator

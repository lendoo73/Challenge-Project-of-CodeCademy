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

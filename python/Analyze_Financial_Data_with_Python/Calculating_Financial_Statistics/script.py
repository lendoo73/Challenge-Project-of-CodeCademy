from math import log

def display_as_percentage(val):
  return "{:.1f}%".format(val * 100)

def calculate_simple_return(start_price, end_price, dividend = 0):
  return (end_price - start_price + dividend) / start_price

def calculate_log_return(start_price, end_price):
  return log(end_price / start_price)

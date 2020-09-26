from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# Write code here
# 2-4. calculating the logarithmic rates of return:
def get_returns(prices):
  returns = []
  for i in range(len(prices) - 1):
    returns.append(calculate_log_return(prices[i], prices[i + 1]))
  return returns

# 5.:
amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

# 6.:
print("Amazon monthly returns: ", ", ".join([display_as_percentage(log_returm) for log_returm in amazon_returns]))
print("Ebay monthly returns: ", ", ".join([display_as_percentage(log_returm) for log_returm in ebay_returns]))

# 7. calculate the annual rate of return:
amazon_annual_returns = sum(amazon_returns)
print("Amazon annual returns: ", display_as_percentage(amazon_annual_returns))
ebay_annual_returns = sum(ebay_returns)
print("Amazon annual returns: ", display_as_percentage(ebay_annual_returns))

# 8. calculating the variance of each stock’s monthly returns:
amazon_variance = calculate_variance(amazon_returns)
ebay_variance = calculate_variance(ebay_returns)
print("The variance for Amazon’s monthly returns is ", amazon_variance)
print("The variance for Ebay’s monthly returns is ", ebay_variance)
print("A greater variance generally signifies a riskier investment.")

# 9. calculate the standard deviation of each stock’s monthly returns:
amazon_std = calculate_stddev(amazon_returns)
ebay_std = calculate_stddev(ebay_returns)
print("The standard deviation of Amazon's monthly returns is ", display_as_percentage(amazon_std))
print("The standard deviation of Ebay's monthly returns is ", display_as_percentage(ebay_std))
print("Amazon’s monthly returns have a greater standard deviation than eBay’s. Investing in Amazon stock is likely riskier.")

# 10. calculate the correlation between the stock returns:
correlation_amazon_ebay = calculate_correlation(amazon_returns, ebay_returns)
print("The correlation between Amason's and Ebay's stock returns is ", correlation_amazon_ebay)
print("there is a moderate positive correlation.")

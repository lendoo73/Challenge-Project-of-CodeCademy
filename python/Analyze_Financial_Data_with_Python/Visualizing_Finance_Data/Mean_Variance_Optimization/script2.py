import pandas as pd
import matplotlib.pyplot as plt
from rf import return_portfolios, optimal_portfolio
import codecademylib3_seaborn
import numpy as np

# 10. Change the path variable
path = 'stock_data_weak.csv'
path = 'stock_data2.csv'
# Load the stock data
stock_data = pd.read_csv(path)

# Find the quarterly for each period
selected=list(stock_data.columns[1:])
returns_quarterly = stock_data[selected].pct_change()

# Find the expected returns 
expected_returns = returns_quarterly.mean()

# Find the covariance 
cov_quarterly = returns_quarterly.cov()

# Find a set of random portfolios
random_portfolios = return_portfolios(expected_returns, cov_quarterly) 

# Plot the set of random portfolios
#random_portfolios.plot.scatter(x='Volatility', y='Returns', fontsize=12)

# Calculate the set of portfolios on the EF
weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

# Plot the set of portfolios on the EF
plt.plot(risks, returns, 'y-o')
plt.ylabel('Expected Returns',fontsize=14)
plt.xlabel('Volatility (Std. Deviation)',fontsize=14)
plt.title('Efficient Frontier', fontsize=24)


# Compare the set of portfolios on the EF to the 
single_asset_std=np.sqrt(np.diagonal(cov_quarterly))
plt.scatter(single_asset_std,expected_returns,marker='X',color='red',s=200)


# 11 & 12. Compare to original
weak_EF = pd.read_csv('weak_risks_returns.csv')
plt.plot(weak_EF['Risks'], weak_EF['Returns'], 'g-o')

strong_EF = pd.read_csv('strong_risks_returns.csv')
plt.plot(strong_EF['Risks'], strong_EF['Returns'], 'k-x')

plt.show()

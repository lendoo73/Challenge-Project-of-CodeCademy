import codecademylib3_seaborn
# 1. import pandas:
import pandas as pd
# 4. import pandas datareader:
import pandas_datareader.data as web
# 5. import datetime module
from datetime import datetime
# 8. import the World Bank sub-module:
import pandas_datareader.wb as wb
# 12. import numpy:
import numpy as np

# 2. import gold prices data:
gold_prices = pd.read_csv("gold_prices.csv")
#print(gold_prices)

# 3. import crude-oil data:
crude_oil_prices = pd.read_csv("crude_oil_prices.csv")
#print(crude_oil_prices)

# 5. create start and end datetimes:
start = datetime(1999, 1, 1)
end = datetime(2019, 1 ,1)
# 6. NASDAQ 100 datas from the FRED API:
nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)
#print(nasdaq_data)

# 7. import data of S&P 500 Index:
sap_data = web.DataReader("SP500", "fred", start, end)
#print(sap_data)

# 9. get GDP data from the World Bank API:
gdp_data = wb.download(
  indicator = "NY.GDP.MKTP.CD",
  country = ["US"],
  start = start,
  end = end
)
#print(gdp_data)

# 10. get data about the value of goods:
export_data = wb.download(
  indicator = "NE.EXP.GNFS.CN",
  country = ["US"],
  start = start,
  end = end
)
#print(export_data)

# 11. :
def log_return(prices):
  # 12: prices: is a single column in a DataFrame
  return np.log(prices / prices.shift(1))

# 13. calcualte the log return of the gold prices:
gold_returns = log_return(gold_prices["Gold_Price"])
#print(gold_returns)

# 14. create log return variables for each additional dataset
crude_oil_returns = log_return(crude_oil_prices["Crude_Oil_Price"])
#print(crude_oil_returns)
nasdaq_data_returns = log_return(nasdaq_data["NASDAQ100"])
#print(nasdaq_data_returns)
sap_data_returns = log_return(sap_data["SP500"])
#print(sap_data_returns)
gdp_data_returns = log_return(gdp_data["NY.GDP.MKTP.CD"])
#print(gdp_data_returns)
export_data_returns = log_return(export_data["NE.EXP.GNFS.CN"])
#print(export_data_returns)

# 15. compare the volatility of each type of data
def display_as_percentage(val):
  return "{:.3f}%".format(val * 100)

print('gold:', display_as_percentage(gold_returns.var()))
print('crude oil:', display_as_percentage(crude_oil_returns.var()))
print('NASDAQ 100:', display_as_percentage(nasdaq_data_returns.var()))
print('S&P 500:', display_as_percentage(sap_data_returns.var()))
print('GDP :', display_as_percentage(gdp_data_returns.var()))
print('Exports:', display_as_percentage(export_data_returns.var()))
print("The S&P 500 has the smallest variance, and thus is the least volatile.")
print("Gold being a stable investment has the second smallest variance.")
print("Crude oil is the most volatile, which makes sense as gas prices are often unpredictable.")
print("Exports are very volatile.")

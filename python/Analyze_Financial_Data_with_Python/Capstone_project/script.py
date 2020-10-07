import tickers
import pure
from stock import Stock
import os
import pandas as pd
import matplotlib.pyplot as plt

os.system("cls")
# ask the user to choose time period:
start, end = tickers.get_period()

# ask the user to create a list of stocks for analisis:
stocks = tickers.create_stock_list(start, end)
os.system("cls")
print("Your choosed the following stocks: ")
Stock.prt()
print("\n")
# columns in df:
# ['close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh', 'adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor']
# Plot the adjusted closing prices over time
for stock in stocks:
    stock_data = stock.get_adjClose()
    plt.plot(stock_data.date, stock_data.adjClose)

plt.xticks(rotation = 70)
plt.xlabel("date")
plt.ylabel("Adjusted Closing Price")
plt.legend(Stock.names)
plt.title("Stocks Adjusted Prices")

plt.show()
plt.close('all')

# Calculate and plot the daily simple rate of return over time:
all_simple_rate_of_returns = []
x = pure.ceil(Stock.length() / 2)
for i in Stock._range():
    plt.subplot(x, 2, i + 1)
    simple_rate_of_return = stocks[i].get_simple_rate_of_return()
    all_simple_rate_of_returns.append(simple_rate_of_return)
    plt.plot(simple_rate_of_return.date, simple_rate_of_return.daily_s_ror)
    plt.xticks(rotation = 70)
    plt.xlabel("date")
    plt.ylabel("Simple ROR")
    plt.title(simple_rate_of_return.symbol[0])

# create common title above all subplot:
plt.tight_layout()
plt.suptitle("Daily simple rate of returns:", fontsize = 16)

plt.show()
plt.close('all')

def plot_bar(list_of_data, name, conclusion1, conclusion2):
    plt.bar(Stock._range(), list_of_data)
    ax = plt.subplot()
    ax.set_xticks(Stock._range())
    ax.set_xticklabels(Stock.names)
    plt.title("{name} of daily simple rate of return".format(name = name))
    plt.ylabel("{name} of simple returns (%)".format(name = name))
    plt.xlabel("Stocks")

    max_data = max(list_of_data)
    index = list_of_data.index(max_data)
    name_max = Stock.names[index]
    min_data = min(list_of_data)
    index = list_of_data.index(min_data)
    name_min = Stock.names[index]
    conclusion_of_data = "{max} has the highest {name}.\n{max} {conclusion1}.\n{min} has the lowest {name} {conclusion2}.".format(max = name_max, min = name_min, name = name, conclusion1 = conclusion1, conclusion2 = conclusion2)
    plt.text(
        0, 
        max_data * 0.8, 
        conclusion_of_data, 
        bbox = dict(
            boxstyle = "square",
            ec = (1, 0.5, 0.5, 0.5),
            fc = (1, 0.8, 0.8, 0.5),
        )
    )

    plt.show()
    plt.close('all')

# Calculate and plot the mean of each stock's daily simple rate of return:
list_of_means = Stock.get_list_of_means(stocks)
conclusion2 = " and the lowest expected return"
if min(list_of_means) < 0:
    # delete stocks with negative mean from the selected portfolio:
    for i in Stock._range():
        if list_of_means[i] < 0:
            Stock.dropped.append(Stock.names[i])

    conclusion2 = " and the expected return is negative.\nNot recommended to invest."

plot_bar(list_of_means, "Mean", "would have been a good choice for investment", conclusion2)
# conclusion after analize mean:

# Calculate and plot the variance:
list_of_variances = Stock.get_list_of_variances(stocks)
plot_bar(list_of_variances, "Variance", " can be a riskier investment", ",indicating that the returns are more predictable.")

# Calculate and plot the standard deviation:
list_of_std = Stock.get_list_of_std(stocks)
plot_bar(list_of_std, "Standard deviation", " can be a riskier investment", ", the safetiest investment but the lowest potential it has for payout.")

# merge the individual simple_rate_of_returns dataframes:
merged_simple_rate_of_returns = pd.concat(all_simple_rate_of_returns).reset_index()

# create a pivot table by reorganizing merged_simple_rate_of_returns
all_stock_pivot = merged_simple_rate_of_returns.pivot(
    columns = "symbol",
    index = "date",
    values = "daily_s_ror"
)

# Calculate the correlations:
correlations = all_stock_pivot.corr()
list_of_names_pairs, list_of_corr_val = stocks[0].get_name_val_from_corr_table(correlations)

# visualize correlations:
num_of_bars = range(len(list_of_names_pairs))
plt.bar(num_of_bars, list_of_corr_val)
plt.xticks(num_of_bars, list_of_names_pairs, rotation = -45)
plt.xlabel("Stocks in pair")
plt.ylabel("Correlation")
plt.title("Correlations between each of the stocks")
max_corr = max(list_of_corr_val)
min_corr = min(list_of_corr_val)
length = len(list_of_names_pairs) - 1
if max_corr > 0.5:
    plt.hlines(y = 0.6, xmin = 0, xmax = length, color = "red", linestyle = '--', label = "positive high correlation")
if max_corr > 0.2:
    plt.hlines(y = 0.3, xmin = 0, xmax = length, color = "yellow", linestyle = '--', label = "positive low correlation")
if min_corr < -0.2:
    plt.hlines(y = -0.3, xmin = 0, xmax = length, color = "orange", linestyle = '--', label = "negative low correlation")
if min_corr < -0.5:
    plt.hlines(y = -0.6, xmin = 0, xmax = length, color = "darkred", linestyle = '--', label = "negative high correlation")
plt.legend()
plt.tight_layout()
plt.show()
plt.close('all')

# Portfolio Optimization:
selected_stocks = all_stock_pivot.reset_index()
if len(Stock.dropped):
    # delete all non selected columns from all_stock_pivot:
    selected_stocks = all_stock_pivot.drop(columns = Stock.dropped).reset_index()

select_cols = list(selected_stocks.columns[1 :])

# Calculate the quarterly returns for the selected_stocks:
quarterly_returns = selected_stocks[select_cols]
# Calculate the mean expected return for each asset:
expected_returns_avg = quarterly_returns.mean()
print(expected_returns_avg)
# Calculate the covariance matrix of the assets:
returns_cov = quarterly_returns.cov()

# calculate 5,000 random portfolios:
print("expected return average", expected_returns_avg)
random_portfolios = pure.return_portfolios(expected_returns_avg, returns_cov)

# plot the random portfolios:
random_portfolios.plot.scatter(
    x = "Volatility",
    y = "Returns"
)
plt.xlabel("Volatility (Std. Deviation)")
plt.ylabel("Expected Returns")
plt.title("Efficient Frontier")

# calculate the efficent frontier:
# index cannot to pass to the optimal_portfolio() !!!
print(quarterly_returns[1 : ])
print(quarterly_returns[1 : ].dropna())
weights, returns, risks = pure.optimal_portfolio(quarterly_returns[1 : ])

def get_portfolio(data, level):
    optimal = pd.DataFrame({"data": data})
    optimal.data = optimal.data.apply(lambda val: round(val, 5))
    if level == "high":
        valmax = optimal.max().data
        first_possible = optimal[optimal.data < valmax].max().data

        def get_high_portfolio(multiplier):
            high_portfolios = random_portfolios[(random_portfolios.Returns < first_possible) & (random_portfolios.Returns > first_possible - (valmax - first_possible) * multiplier)]
            try:
                portfolio = high_portfolios.loc[high_portfolios.Volatility.idxmin()]
                return portfolio
            except:
                return get_high_portfolio(multiplier + 1)
            
        
        portfolio = get_high_portfolio(3)
        
    elif level == "low":
        valmin = optimal.min().data
        first_possible = optimal[optimal.data > valmin].min().data
        def get_low_portfolio(multiplier):
            low_portfolios = random_portfolios[(random_portfolios.Volatility > first_possible) & (random_portfolios.Volatility < first_possible - (valmin - first_possible) * multiplier)]
            try:
                portfolio = low_portfolios.loc[low_portfolios.Returns.idxmax()]
                return portfolio
            except:
                return get_low_portfolio(multiplier + 1)
        
        portfolio = get_low_portfolio(4)

    weight = portfolio.iloc[2 : ]
    volatility = portfolio.Volatility
    returns = portfolio.Returns

    return weight, volatility, returns

def create_marker(x, y, txt):
    plt.scatter(
        x,
        y, 
        marker = "X",
        color = "orange",
        s = 200
    )
    # add label to the X marker:
    plt.text(
        x + 0.0002, 
        y,
        txt, 
        bbox = dict(
            boxstyle = "square",
            ec = (1, 0.5, 0.5, 0.5),
            fc = (1, 0.8, 0.8, 0.5),
        )
    )

# find a high risk portfolio:
high_risk_weight, x_high, y_high = get_portfolio(returns, "high")
# show the high risk portfolio on scatter plot:
create_marker(x_high, y_high, "High risk")

# find low risk portfolio:
low_risk_weight, x_low, y_low = get_portfolio(risks, "low")
create_marker(x_low, y_low, "Low risk")

# find moderate risk portfolio:
x_mean = (x_high + x_low) / 2
def get_moderate_portfolio(multiplier):
    moderate_portfolios = random_portfolios[(random_portfolios.Volatility > x_mean - multiplier) & (random_portfolios.Volatility < x_mean + multiplier)]
    try:
        print("moderate_portfolios: ", moderate_portfolios)
        portfolio = moderate_portfolios.loc[moderate_portfolios.Returns.idxmax()]
        print("portfolio: ", portfolio)
        return portfolio
    except:
        return get_moderate_portfolio(multiplier + 0.0001)
portfolio = get_moderate_portfolio(0.0001)
moderate_risk_weight = portfolio.iloc[2 : ]
x_mod = portfolio.Volatility
y_mod = portfolio.Returns
create_marker(x_mod, y_mod, "Moderate risk")


# plot the efficient frontier as a yellow line:
plt.plot(risks, returns, 'y-o')

# remove data of dropped stocks from expected returns (list_of_means) and list_of_std:
for drop in Stock.dropped:
    i = Stock.names.index(drop)
    list_of_std.pop(i)
    list_of_means.pop(i)
    Stock.names.pop(i)

# add red X marks to display the volatility and expected return for each individual asset:
for i in range(len(list_of_means)):
    x = list_of_std[i] / 100
    y = list_of_means[i] / 100
    plt.scatter(
        x,
        y, 
        marker = "X",
        color = "red",
        s = 200
    )
    # add label to the X marker:
    plt.text(
        x + 0.0002, 
        y,
        Stock.names[i]
    )

plt.show()
plt.close('all')

# create pie charts:
labels = list(high_risk_weight.index.str.replace(" Weight", "", regex = True).values)
plt.subplot(2, 2, 1)
plt.suptitle("Recomended portfolios:", fontsize = 16)
# create pie chart of high risk portfolio:
plt.pie(high_risk_weight.values, autopct = "%1.1f%%", labels = labels)
plt.xlabel("High Risk portfolio")


# create pie chart of low portfolio
plt.subplot(2, 2, 2)
plt.pie(low_risk_weight.values, autopct = "%1.1f%%", labels = labels)
plt.xlabel("Low Risk portfolio")

# create pie chart of moderate portfolio
plt.subplot(2, 2, 3)
plt.pie(moderate_risk_weight.values, autopct = "%1.1f%%", labels = labels)
plt.xlabel("Moderate Risk portfolio")
plt.tight_layout()
plt.show()

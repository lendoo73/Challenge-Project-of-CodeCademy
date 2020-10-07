import numpy as np
import pandas as pd
import cvxopt as opt
from cvxopt import blas, solvers

def ceil(num):
    ceil_num = int(num)
    return ceil_num if ceil_num == num else ceil_num + 1

# This function accepts the expected returns and covariance matrix for a collection of assets. The function returns a DataFrame with 5,000 portfolios of random asset weights:
def return_portfolios(expected_returns, cov_matrix):
    np.random.seed(1)
    port_returns = []
    port_volatility = []
    stock_weights = []
        
    selected = (expected_returns.axes)[0]
        
    num_assets = len(selected) 
    num_portfolios = 5000
        
    for single_portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        returns = np.dot(weights, expected_returns)
        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        port_returns.append(returns)
        port_volatility.append(volatility)
        stock_weights.append(weights)
        
        portfolio = {'Returns': port_returns,
                    'Volatility': port_volatility}
        
    for counter,symbol in enumerate(selected):
        portfolio[symbol +' Weight'] = [Weight[counter] for Weight in stock_weights]
        
    df = pd.DataFrame(portfolio)
        
    column_order = ['Returns', 'Volatility'] + [stock+' Weight' for stock in selected]
        
    df = df[column_order]
    
    # Each portfolio includes the following columns:
    # 'Returns' — the expected return of the portfolio
    # 'Volatility' — the standard deviation of the portfolio
    # 'Weight Asset 1' … 'Weight Asset N' — the weights of each asset in the given portfolio.

    return df

def optimal_portfolio(returns):

    # returns — the returns for all assets over a specified timeframe
    # index cannot to pass to the optimal_portfolio() !!!
    n = returns.shape[1]
    #returns = np.transpose(returns.as_matrix())
    returns = np.transpose(returns.to_numpy())

    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]

    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))
    pbar = opt.matrix(np.mean(returns, axis=1))

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n ,1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)

    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x']
                  for mu in mus]
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']

    # The function returns:
        # weights — the weights for each asset in the portfolio
        # returns — the expected returns of each portfolio
        # risks — the risk of each portfolio, measured as standard deviation
    return np.asarray(wt), returns, risks

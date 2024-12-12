
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.optimize as optimization
from matplotlib.font_manager import weight_dict

pd.set_option('display.max_columns', 7)
# on average there are 252 trading days in year
NUM_TRADING_DAYS = 252

# stocks we are going to handle
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']

# historical data -define START and END
start_date = '2012-01-01'
end_date = '2017-01-31'

def download_data():
    # Key = name, value = stock value

    stock_data = pd.DataFrame()

    for stock in stocks:
        # closing prices

        # ticker is object of class Ticker, stock is passed to class
        ticker = yf.Ticker(stock)

        # calling method history from class Ticker on instance ticker, saving results in data DataFrame
        data = ticker.history(start = start_date, end = end_date)


        if not data.empty:
            stock_data[stock] = data['Close']

    return stock_data

def show_data(data):
    data.plot(figsize = (10,5))
    plt.show()

def calculate_return(data):
    log_return =  np.log(data/data.shift(1))
    return log_return
    # print(log_return[1:])

def show_statistics(returns):
    # instead of daily, we are after annual
    print(returns.mean() * NUM_TRADING_DAYS)
    print(returns.cov() * NUM_TRADING_DAYS)

def show_mean_variance(returns, weights):
    # for annual return
    portfolio_return = np.sum(returns.mean()*weights) * NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(
                returns.cov() * NUM_TRADING_DAYS, weights
            )
        )
    )
    print("Expected portfolio mean (return):", portfolio_return)
    print("Expected portfolio mean (return):", portfolio_volatility)


if __name__ == '__main__':

    # download_data()
    dataset = download_data()
    # show_data(dataset)

    log_daily_returns = calculate_return(dataset)
    # show_data(log_daily_returns)

    show_statistics(log_daily_returns)
    show_mean_variance(log_daily_returns)

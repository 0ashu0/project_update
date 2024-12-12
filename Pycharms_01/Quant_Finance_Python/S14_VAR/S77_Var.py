import numpy as np
import yfinance as yf
from scipy.stats import norm
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def download_data(stock, start_date, end_date):
    data = pd.DataFrame()
    ticker = yf.download(stock, start_date, end_date)
    # print(ticker.columns)
    # data = ticker[['Price Ticker Date', 'Adj Close']]
    data[stock] = ticker['Adj Close']

    return data

def display_stock(stock):
    plt.title("Plot of City stocks")
    plt.xlabel("Year")
    plt.ylabel("Stock Price")
    # plt.xlim(0, np.max(stock_data['Date']))
    # plt.ylim(0, np.max(stock_data['C']))
    plt.plot(stock)
    plt.show()

# this is just for tomorrow
def calculate_var(position, c, mu, sigma):
    # c confidence level, 95% or 99%
    v = norm.ppf(1-c)
    var = position * (mu - sigma * v)
    return var

# var for any days in future
def calculate_var_n(position, c, mu, sigma, n):
    # n is number of days
    # c confidence level, 95% or 99%
    v = norm.ppf(1-c)
    var = position * (mu*n - sigma * np.sqrt(n) * v)
    return var

if __name__ == '__main__':

    start = datetime.datetime(2024, 11, 1)
    end = datetime.datetime(2024, 12, 9)
    stock_data = download_data('NETWEB.NS', start, end)
    # print(stock_data)
    # display_stock(stock_data)
    # print(stock_data.shape)
    # print(str(stock_data))
    # print(stock_data.columns)

    # taking log of daily returns
    stock_data['returns'] = np.log(stock_data['NETWEB.NS'] / stock_data['NETWEB.NS'].shift(1))
    stock_data = stock_data[1:]
    print(stock_data)


    # investment
    S = 20000
    # confidence level - set to 95%
    c = 0.95

    # we assume that daily returns are normally distributed
    mu = np.mean(stock_data['returns'])
    sigma = np.std(stock_data['returns'])

    print(calculate_var(S, c, mu, sigma))

    print(calculate_var_n(S, c, mu, sigma, 10))
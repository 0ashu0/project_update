
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.optimize as optimization

pd.set_option('display.max_columns', 7)


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

if __name__ == '__main__':

    # download_data()
    dataset = download_data()
    show_data(dataset)


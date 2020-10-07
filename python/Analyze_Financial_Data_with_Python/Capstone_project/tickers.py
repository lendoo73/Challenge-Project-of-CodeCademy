from stock import Stock
import pandas as pd
import os
from datetime import datetime, date
import pandas_datareader.data as web

# https://apimedia.tiingo.com/docs/tiingo/daily/supported_tickers.zip
# create a list from the supported tickers by Tiingo:
supported_tickers = list(pd.read_csv("supported_tickers.csv")[pd.read_csv("supported_tickers.csv").ticker >= "A"].reset_index().ticker)
#print(supported_tickers)

def choose_ticker():
    
    # ask the user to enter a stock-name; if the given ticker is valid return it, else return False
    ticker = input("Please add any stock to your list: ").upper()
    if ticker in supported_tickers:
        return ticker
    elif ticker !=  "":
        print(ticker, "is not a valid stock's name.")
        return False

def create_stock_list(start, end):
    # this function create list with minimum 4 valid and unique stocks:
    print("To analize stocks, please add minimum 4 stocks to the list.")
    print("When you finished, press ENTER.")

    stocks = []
    userinput = " "
    # ask the user to select some stocks:
    while True:
        userinput = choose_ticker()
        # check if the emtered stock is valid:
        if userinput:
            if userinput not in Stock.names:
                # this stock is not in the list, add to the list
                df = get_dataset(userinput, start, end)
                if df:
                    # tiingo sent the dataset:
                    stocks.append(df)
                    os.system("cls")
                else:
                    # any error occured while queried data from tiingo:
                    os.system("cls")
                    print("This ticker '", userinput, "' currently unavailable, please choose another one.")
            else:
                # this stock already in the list, let's remove it
                print(userinput)
                print(stocks)
                for i in range(len(stocks)):
                    if stocks[i].name == userinput:
                        stocks.pop(i)
                        print(userinput, "deleted from your list.")
                        Stock.names.remove(userinput)
                        break
            # print the selected stocks:
            print("Your selected stocks: ")
            #print(*Stock.names, sep = ", ")
            Stock.prt()
            if len(stocks) < 4:
                print("Please choose more ", 4 - len(stocks))
            else:
                print("Press ENTER or add more stcoks...")
        # check if the user finished:
        if userinput == None and len(stocks) >= 4:
            return stocks

def get_period():
    # ask the user to choose 1, 2 or 3 (year) for data analize; return 'start' and 'end' timeobject
    print("    1. Short time period: analize the last year only")
    print("    2. Middle time period: analize 3 year")
    print("    3. Long time period: analize 5 year")
    while True:
        period = input("Please choose a time period for analize your choosen stocks ( 1 - 3 ): ")
        if period != "1" and period != "2" and period != "3":
            print("Only 1, 2 or 3 allowed.")
        else:
            year = 1 if period == "1" else 3 if period == "2" else 5
            end = datetime.timestamp(datetime.now())
            years_in_timestamp = 60 * 60 * 24 * 365 * year
            return datetime.fromtimestamp(end - years_in_timestamp), datetime.fromtimestamp(end)

def get_dataset(ticker, start, end):
    try:
        df = web.get_data_tiingo(
            ticker, 
            api_key = os.getenv('TIINGO_API_KEY'), 
            start = start, 
            end = end
        )

        # if data not available from start date, refuse the coosen stock:
        start_plus_one = start + pd.DateOffset(days = 1)
        ts_start = datetime.timestamp(start_plus_one)
        ts_first_available_data = datetime.timestamp(df.index[0][1])
        if ts_first_available_data > ts_start:
            return False
        # if data not available till today, refuse the choosen stock:
        lastdate_plus_one = df.index[-1][1] + pd.DateOffset(days = 1)
        end_minus_one = end + pd.DateOffset(days = -1)
        ts_lastdate = datetime.timestamp(lastdate_plus_one)
        ts_end = datetime.timestamp(end_minus_one)
        if ts_lastdate < ts_end:
             return False
        return Stock(ticker, df)
    except:
        return False
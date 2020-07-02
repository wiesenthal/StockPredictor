import numpy as np
import matplotlib.pyplot as plt
#import mltools as ml
from pandas_datareader import data as pdr
from datetime import date, datetime, timedelta
import yfinance as yf
#import fix_yahoo_finance as yf
import pandas as pd

import sys

numRequests = 0

def getFinanceData(fileName):#financial documents, not stock price
    #df = np.genfromtxt(fileName, delimiter='\t', dtype= (float, float, float, "|S10", "|S10", float, float, float))
    df = pd.read_csv(fileName, sep="\t", header=None)
    df[3] = pd.to_datetime(df[3], yearfirst=True)
    df.sort_values(3, axis=0, inplace=True)    
    return df

def byDate(df):
    prevDate = df[3].values[0]
    output = []
    sameDateTickers = []
    
    for currDate, ticker in zip(df[3].values, df[4].values):
        if(currDate == prevDate):
            sameDateTickers.append(ticker)
        else:
            
            #print(sameDateTickers)
            data_dict = getData(sameDateTickers, prevDate)
            for t in sameDateTickers:
                output.append(data_dict[t])
            #print("\n\n" + str(prevDate) + "\n\n")
            prevDate = currDate
            sameDateTickers = [ticker]
    data_dict = getData(sameDateTickers, prevDate)
    for t in sameDateTickers:
        output.append(data_dict[t])
    return output
        
def saveDF(df, filename):
    df.to_csv(filename, sep="\t")

def dateToString(date):
    return pd.to_datetime(str(date)).strftime("%Y-%m-%d")

def nextDay(inpDate):
    return inpDate + np.timedelta64(1,'D')
    
def getData(ticker, date):
    global numRequests
    numRequests += 1
    if(numRequests % 10 == 0):
        print("\n\n\nNumber of Requests: {},\nDate: {}\n\n".format(numRequests, date))
    #print(ticker)
    #data = pdr.get_data_yahoo("AAPL", start=date, end=date)
    #print("Start Date: {}\tNext Day: {}".format(dateToString(date), dateToString(nextDay(date))))
    
    data = yf.download(ticker, start=dateToString(date), end=dateToString(nextDay(date)), threads=False) #,threads=True
    d = {}
    if(data.empty):
        for i in ticker:
            d[i] = np.nan
        return d
        #return [np.nan]*len(ticker)

    if len(ticker) == 1:
        print(ticker[0], data['Adj Close'][0])
        d[ticker[0]] = data['Adj Close'][0]
    else:
        for i in data['Adj Close'].keys():
            d[i] = data['Adj Close'][i].values[0]
            
    #closeVal = data['Adj Close'].values.tolist()
    
    #while type(closeVal[0]) is list:
    #    closeVal = closeVal[0]
    #openVal = data['Open'].values[0]
    #data_name=ticker + '_' + end_date
    return d

if __name__ == '__main__':
    print(sys.argv[1])
    fileName = sys.argv[1] + '.tsv' #"last.tsv"
    df = getFinanceData(fileName)
    print("byDate")
    out = byDate(df)
    df['price'] = out
    df.dropna(inplace=True)
    saveDF(df, sys.argv[1] + '_out.tsv')
    print("Num Requests at End: ", numRequests)

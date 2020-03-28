# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:01:26 2020

@author: harishangaran

The following script plots the cummulative return of stocks.

Call the class and input your list of stocks and period to plot
the cummulative graph.
    eg: cummulativeReturn(['AAPL','GOOG','FB','AMZN'],'252d').plotGraph(size=(16,6))

Change the size of the graph by changing the size attribute.
By default it is (16,6)

Visualise how much $1 invested over a period would have returned.

"""
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

class cummulativeReturn:
    def __init__(self,stocklist,period):
        self.stocklist = stocklist
        self.period = period
        self.callPrices()
        self.plotGraph()
        
    def callPrices(self):
        
        # Calling the price from yahoo finance
        listOfStocks = [yf.Ticker(i).history(period=self.period
                                             ) for i in self.stocklist]
        
        #calculate returns for all stocks
        for stocks in range(len(listOfStocks)):
            listOfStocks[stocks]['rs'] = listOfStocks[
                                            stocks]['Close'].pct_change(1)

        #calculate cummulative returns
        for stocks in range(len(listOfStocks)):
            listOfStocks[stocks]['cumm returns'] = (1 + 
                                    listOfStocks[stocks]['rs']).cumprod()
        
        # Zipping the stock names as keys of a dictionary
        self.listOfStocksDict = dict(zip(self.stocklist,listOfStocks ))
        
        # Appending all close prices to a list of series
        listOfCummReturns = []
        for i in range(len(self.stocklist)):
            listOfCummReturns.append(self.listOfStocksDict[
                self.stocklist[i]]['cumm returns'])
            
        # Concating the list of series to a pandas dataframe
        self.listToPlot = pd.concat(listOfCummReturns,axis=1)
        self.listToPlot.columns = self.stocklist
        
    def plotGraph(self,size=(16,6)): #must give a default value for args
        self.size = size
        plt.style.use('ggplot')
        self.listToPlot.plot(figsize=(self.size))
        plt.title('How much $1 invested in these stocks returns you over a period of {}'.format(self.period))
        plt.ylabel('($)')
        
cummulativeReturn(['AAPL','GOOG','FB','AMZN'],'252d').plotGraph((16,6))

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:05:54 2020

@author: harishangaran

SCATTER MATRIX PLOT

Visulalisation of relationships between stocks using scatter matrix plot

Simply call the class and give the list of your preferred stocks and the
length of the period.

    eg: plotScatterMatrix(['MSFT','AMZN','AAPL'],'252d')

Stock prices are pulled from yahoo finance.
    eg '252d' calls the last 252 days trade prices

Get any ticker symbol of any stocks from yahoo finance and run your 
correlation scatter matrix.
"""

import pandas as pd
import yfinance as yf

from pandas.plotting import scatter_matrix


class plotScatterMatrix:
    def __init__(self,stocklist,period):
        self.stocklist = stocklist
        self.period = period
        self.callPrices()
        self.scatter_matrix()
        
    def callPrices(self):
        
        # Calling the price from yahoo finance
        listOfStocks = [yf.Ticker(i).history(period=self.period
                                             ) for i in self.stocklist]
        
        # Zipping the stock names as keys of a dictionary
        self.listOfStocksDict = dict(zip(self.stocklist,listOfStocks ))
        
        # Appending all close prices to a list of series
        listOfClosePrices = []
        for i in range(len(self.stocklist)):
            listOfClosePrices.append(self.listOfStocksDict[
                self.stocklist[i]]['Close'])
            
        # Concating the list of series to a pandas dataframe
        self.listToPlot = pd.concat(listOfClosePrices,axis=1)
        self.listToPlot.columns = self.stocklist
        return self.listToPlot
    
    def scatter_matrix(self):
        
        # Plotting the scatter matrix of the list of stocks
        # using built-in pandas.plotting module
        scatter_matrix(self.listToPlot,figsize=(10,10),alpha=0.5)

plotScatterMatrix(['MSFT','AMZN','AAPL'],'252d')

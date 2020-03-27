# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:02:42 2020

@author: harishangaran

Candle Stick Plot Using Matplotlib
"""
import matplotlib.pyplot as plt
import yfinance as yf

from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter,date2num,WeekdayLocator,DayLocator,MONDAY

# Calling price from yahoo finance
# Change ticker code and period
ford = yf.Ticker('MSFT').history(period='100d')

# Reseting index of the dataframe
ford_reset = ford.loc[:].reset_index()

#adding date axes column and converting date to a num
ford_reset['date_ax'] = ford_reset['Date'].apply(lambda date: date2num(date))

list_of_cols = ['date_ax','Open','High','Low','Close']
ford_values = [tuple(vals) for vals in ford_reset[list_of_cols].values]

mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')

fig, ax = plt.subplots(figsize=(20,6))
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, ford_values,width=0.5,colorup='g',colordown='r')

"""

Adapted from Python for Finance by Yves Hilpisch (2014).

Simple example of volatility analysis on GOOG shares
during the past 5 years. Data obtained from Google
Finance. Rolling standard deviation of log returns is
calculated. Results are subsequently plotted against daily close prices.

"""

import matplotlib.pyplot as plt
import numpy as np        
import pandas as pd        
import pandas_datareader.data as web

goog = web.DataReader('GOOG', data_source='google',
                      start='2/15/2013', 
                      end='2/15/2018')

print goog.tail()

goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = (goog['Log_Ret'].rolling(window=252,center=False).std()) * np.sqrt(252)
      
      
fig = plt.figure()

p1 = fig.add_subplot(221)
p1.plot(goog['Close'], color='blue')

p2 = fig.add_subplot(222)
p2.plot(goog['Volatility'], color='red')

plt.savefig('volatility.eps')
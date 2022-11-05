import yfinance as yf

import numpy as np
import pandas as pd
#define the ticker symbol
tickerSymbol_1 = 'AMD'
tickerSymbol_2 = 'NVDA'

#get data on this ticker
tickerData_1 = yf.Ticker(tickerSymbol_1)
tickerData_2 = yf.Ticker(tickerSymbol_2)

#get the historical prices for this ticker
df_AMD = tickerData_1.history(period='1d', start='2022-1-1', end='2022-10-6')
df_NVDA = tickerData_2.history(period='1d', start='2022-1-1', end='2022-10-6')

#see your data
print(df_AMD)
print(df_NVDA)

close_AMD = df_AMD["Close"]
close_NVDA = df_NVDA["Close"]

close = pd.DataFrame({
    'close_AMD':df_AMD["Close"],
    'close_NVDA':df_NVDA["Close"]
})
print(close)

#print(close_AMD)
#print()

simple_return = close.pct_change()
log_return = np.log(1+simple_return)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt   # Import matplotlib
# This line is necessary for the plot to appear in a Jupyter notebook
# %matplotlib inline
# Control the default size of figures in this Jupyter notebook
# %pylab inline

   # Change the size of plots

#apple["Adj. Close"].plot(grid = False) # Plot the adjusted closing price of AAPL

simple_return.plot()
plt.show()

log_return.plot()
plt.show()

plt.plot(simple_return,log_return, 'o',c='blue')
plt.ylabel( 'Log-return' )
plt.xlabel( 'Simple return' )
#plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True)

plt.show()

import seaborn as sns

# histogram
sns.distplot(log_return, kde=False, norm_hist=True,label='Log-returns')
sns.distplot(simple_return, kde=False, norm_hist=True, label='Simple returns')

plt.legend(loc='upper left')

# plt.tight_layout()
# plt.savefig('images/ch1_im10.png')
plt.show()

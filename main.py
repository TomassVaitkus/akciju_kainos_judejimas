# informacijos saltinis https://pythonprogramming.net


import pandas as pd
import pandas_datareader as web
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')
# stock_id = ['IBM', 'TSLA', 'GOOGL', 'FB', 'AAPL']
# reikia talpinti daugiau akciju ID, kad ivedus GUI input laukelyje akcijos ID ismestu rezultata  tos akcijos grafika

start = dt.datetime( 2019,1,1)
end = dt.datetime(2019,6,1)

df = web.DataReader('TSLA', 'yahoo', start, end)
df.to_csv('TSLA.csv')

df = pd.read_csv('TSLA.csv', parse_dates = True, index_col = 0)
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])


plt.show()

# df1 = web.DataReader('TSLA', 'yahoo', start, end)


# one_entry = [stock_id, open_price, close_price, price_low, price_max, volume]

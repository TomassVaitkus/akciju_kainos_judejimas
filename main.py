# informacijos saltinis https://pythonprogramming.net


import pandas as pd
import pandas_datareader as web
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')

# nusistatom pradžios ir pabaigos datą
start = dt.datetime( 2019,1,1)
end = dt.datetime(2019,6,1)

# susirenkam ir išsisaugom duomenis i failą
df = web.DataReader('TSLA', 'yahoo', start, end)
df.to_csv('TSLA.csv')

# Atidarom failą
df = pd.read_csv('TSLA.csv', parse_dates = True, index_col = 0)
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# Ši vieta nebūtina, tik isitikinimui,kad nuskaito
print(df.head())
# nustatome, kokius duomenis norime matyti, koks periodas
df_ohlc = df["Adj Close"].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()


# Suformuojame patį grafiką, žvakės, dydžiai, standartinės spalvos
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup='black')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

# Atvaizduojame

plt.show()



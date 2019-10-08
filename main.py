import pandas as pd
import pandas_datareader as web
import datetime as dt
from matplotlib import style

style.use('ggplot')
# stock_id = ['IBM', 'TSLA', 'GOOGL', 'FB', 'AAPL']
# reikia talpinti daugiau akciju ID, kad ivedus GUI input laukelyje akcijos ID ismestu rezultata  tos akcijos grafika

start = dt.datetime( 2019,1,1)
end = dt.datetime(2019,6,1)

df = web.DataReader('IBM', 'yahoo', start, end)
print(df.head())

df1 = web.DataReader('TSLA', 'yahoo', start, end)
print(df1.head())
#
# one_entry = [stock_id, open_price, close_price, price_low, price_max, volume]

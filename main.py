import datetime as dt
import yfinance as yf
import mplfinance as mpf

crypto='BTC'
currency='USD'
start=dt.datetime.now()-dt.timedelta(days=365)
end=dt.datetime.now()
data=yf.download(f'{crypto}-{currency}',start=start,end=end)
mpf.plot(data,type='candle',volume=True,style='yahoo')

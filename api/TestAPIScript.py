import datetime
import yfinance as yf

data = yf.Ticker("BTC-USD")
data = data.history(period="1d", interval="1h")
print(data.tail())
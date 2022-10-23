from operator import eq
import pandas as pd
import pandas_ta as ta
import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf


df = pd.DataFrame()

#df = df.ta.ticker("^FVX")
#df.to_csv('./StockDataCSV/5YUST_StockData.csv')

#names = yf.Tickers('^FVX ^TNX CL=F DX-Y.NYB GC=F ^GSPC BTC-USD')

#data = yf.download('^FVX ^TNX CL=F DX-Y.NYB GC=F ^GSPC BTC-USD', start="2017-08-01",end="2022-07-31")
#data.to_csv('./StockDataCSV/EquityData.csv')

equityData = pd.read_csv('./StockDataCSV/EquityData.csv', sep=',', index_col=0, usecols=[0,1,2,3,4,5,6,7])
equityData.dropna(inplace=True)
equityData.columns = ['UST5Y', 'UST10Y', 'BrentCrude', 'DollarIDX', 'Gold', 'SNP500', 'BTCUSD']
print(equityData.info())
print(equityData.head())

# equityData.plot(x = equityData['UST5Y'], y = equityData['BrentCrude'])
# plt.plot(x = equityData['Date'], y = equityData['BrentCrude'])
plt.plot(equityData['BrentCrude'])
plt.show()

#### READ FROM THE CSV FILES
# ust5YData      = pd.read_csv('./StockDataCSV/5YUST_StockData.csv', sep=',')
# ust10YData     = pd.read_csv('./StockDataCSV/10YUST_StockData.csv', sep=',')
# brentCrudeData = pd.read_csv('./StockDataCSV/BrentCrude_StockData.csv', sep=',')
# dollarIdxData  = pd.read_csv('./StockDataCSV/DollarIndex_StockData.csv', sep=',')
# goldData       = pd.read_csv('./StockDataCSV/Gold_StockData.csv', sep=',')
# snp500Data     = pd.read_csv('./StockDataCSV/GSPC_SNP500_StockData.csv', sep=',')

#### CLEAN DATA TO CONTAIN ON THE MAX OF SIZE OF THE SMALLEST DATAFRAME
# ust5YData = ust5YData.tail(3740)
# ust10YData = ust10YData.tail(3740)
# dollarIdxData = dollarIdxData.tail(3740)
# goldData = goldData.tail(3740)
# snp500Data = snp500Data.tail(3740)

#### SET INDEX FOR PANDAS_TA STRATEGY AND APPLY ALL STRATEGY
# brentCrudeData.set_index(pd.DatetimeIndex(brentCrudeData["Date"]), inplace=True)
# dollarIdxData.set_index(pd.DatetimeIndex(dollarIdxData["Date"]), inplace=True)
# goldData.set_index(pd.DatetimeIndex(goldData["Date"]), inplace=True)
# snp500Data.set_index(pd.DatetimeIndex(snp500Data["Date"]), inplace=True)

# brentCrudeData.ta.strategy()
# dollarIdxData.ta.strategy()
# goldData.ta.strategy()
# snp500Data.ta.strategy()

#### REMOVE ANY COLUMNS WITH ALL NAN
# brentCrudeData.dropna(axis=1, how='all', inplace=True)
# dollarIdxData.dropna(axis=1, how='all', inplace=True)
# goldData.dropna(axis=1, how='all', inplace=True)
# snp500Data.dropna(axis=1, how='all', inplace=True)

#### REMOVE ANY ROWS WITH ANY NAN
# brentCrudeData.dropna(inplace=True)
# dollarIdxData.dropna(inplace=True)
# goldData.dropna(inplace=True)
# snp500Data.dropna(inplace=True)

# print("\n#### AFTER DROPNA #####")
# print(brentCrudeData.info())
# print(dollarIdxData.info())
# print(goldData.info())
# print(snp500Data.info())
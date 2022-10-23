##################### HELPER FUNCTIONS #####################

def getBitcoinValue():
   #Getting the data from the API
   url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
   response = requests.get(url)
   data = response.json()
   return float(data['bpi']['USD']['rate'].replace(",", ""))

##################### IMPORT STATEMENTS #####################

from multiprocessing.dummy import active_children
import os
import warnings

import openpyxl
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

##### TENSORFLOW
from tensorflow import keras

##### SKLEARN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

##### OTHER IMPORTS
from pathlib import Path
import datetime
import yfinance as yf
import pandas as pd
import numpy as np
from operator import eq
import random
import requests

##################### READ EXCEL FILE AND GENERATE "DATA" #####################

data = pd.read_excel('StockDataCSV/BTCBotData-Hourly.xlsx', engine='openpyxl')['Adj Close']

data = np.array(data)
data = np.reshape(data, (-1, 1))

train_data, test_data = train_test_split(
    data, train_size=0.8, test_size=0.2, shuffle=False)
scaler = MinMaxScaler()
scaled_train_data = scaler.fit_transform(train_data)
scaled_test_data = scaler.transform(test_data)

##################### CREATE VARIABLE USED FOR FUTURE PREDICTION #####################

std = pd.read_excel('StockDataCSV/Hourly_Start_Data_new.xlsx', engine='openpyxl')

reader = pd.read_excel(r'newTest.xlsx', engine='openpyxl')
print(len(reader))
print(reader)

##################### IMPORT MODEL FROM PREDEFINED H5 #####################

model = keras.models.load_model('results/lstm_time_series/model_hourly.h5')

##################### PREDICT THE NEXT VALUE #####################

m = []
m.append(std[std.size-60:std.size])
m1 = np.array(m)
m2 = np.reshape(m1, (m1.shape[0], m1.shape[1], 1))
p = model.predict(m2)

### GET ACTUAL VALUE
actualValue = getBitcoinValue()
avreshape = np.reshape(actualValue, (-1, 1))
std = np.append(std, scaler.transform(avreshape))
std = np.reshape(std, (-1, 1))

df = pd.DataFrame(scaler.transform(avreshape))
pathfile = 'newTest.xlsx'
with pd.ExcelWriter(path) as writer:
    writer.book = openpyxl.load_workbook(pathfile)
    df.to_excel(writer)
#writer = pd.ExcelWriter('newTest.xlsx', engine='xlsxwriter')
#df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=2)
#writer.save()

pr = scaler.inverse_transform(p).flatten()
av = actualValue

##################### APPEND TO CSV TYPE FILE #####################
#pd.DataFrame(pr).to_csv("results/MinutePrediction.csv")
#pd.DataFrame(av).to_csv("results/MinuteActual.csv")
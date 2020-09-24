import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from darts import TimeSeries
import matplotlib.pyplot as plt
import darts.utils
from darts import utils as utils
from darts.models import RNNModel
import datetime
import warnings
warnings.filterwarnings("ignore")
from darts.utils.missing_values import auto_fillna

import statsmodels
df = pd.read_csv('alv.csv')
df
df.plot()
plt.show()
df.describe()
X = df['Open']
diff = list()
for i in range(1, len(X)):
    value = X[i]-X[i-1]
    diff.append(value)
    
plt.plot(diff)
plt.show()
df.describe()
X = df['Open']
diff = list()
for i in range(1, len(X)):
    value = X[i]-X[i-1]
    diff.append(value)
    
plt.plot(diff)
plt.show()

X = np.reshape(X, (len(X), 1))
y = df["Open"].values

model = LinearRegression()
model.fit(X, y)
# calculate trend
trend = model.predict(X)
# plot trend
plt.xlabel('Date')
plt.ylabel('Open')
plt.plot(y)
plt.plot(trend)
plt.show()

# detrend
detrended = [y[i]-trend[i] for i in range(0, len(y))]
# plot detrended
plt.xlabel('Date')
plt.ylabel('Number of air passengers')
plt.plot(detrended)
plt.show()

db = client.db_financial_markets
col_price_history = db["price_history"]
lstm_prediction_history = db["predictions"]

with open('companies_of_interest.txt') as f:
    lst_tickers_of_interest = [line.strip() for line in f.readlines()]

def make_lstm_prediction():
    for ticker in lst_tickers_of_interest:
        df_ticker = pd.DataFrame(list(col_price_history.find({'Ticker':ticker})))[["DailyChangePct","Date"]].set_index('Date')
        df_ticker.index = pd.to_datetime(df_ticker.index)
        df_ticker = df_ticker.reindex(index=df_ticker.index[::-1])
        series = TimeSeries.from_dataframe(df_ticker, time_col = None,value_cols='DailyChangePct',freq='B',fill_missing_dates=True)
        series = auto_fillna(series)

        SEQ_LENGTH = 6
        HIDDEN_SIZE = 5
        OUTPUT_LEN = 1
        NUM_LAYERS = 1

        model = RNNModel(
            model='LSTM',
            output_length=OUTPUT_LEN,
            hidden_size=HIDDEN_SIZE,
            n_rnn_layers=NUM_LAYERS,
            input_length=SEQ_LENGTH,
            batch_size=16,
            n_epochs=10,
            optimizer_kwargs={'lr': 1e-3}, 
            model_name=f'{ticker}_RNN', log_tensorboard=False
        )

        model.fit(series)
        lstm_prediction = model.predict(1).values()[0][0]
        lstm_prediction_history.insert_one({"Date":datetime.datetime.today(), "Ticker":ticker, "LSTM_prediction" : float(lstm_prediction)})
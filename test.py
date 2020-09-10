import yfinance as yf
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.db_financial_markets
col_price_history = db["price_history"]

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["finance"]
mycol = mydb["mycollection"]

data_from_db = mycol.find_one({"index":"SPY"})
output_dataframe = pd.DataFrame(data_from_db["data"])
output_dataframe.set_index("Date",inplace=True)
print(output_dataframe)

# db.Trading.remove({})
print(db.Trading.find_one())
print(db.Trading.count())


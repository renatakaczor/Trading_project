import yfinance as yf
msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

1

# get historical market data


2

hist = msft.history(period="30d")


3

hist
data_df = yf.download("ALV", start="2015-02-01", end="2015-03-20")
data_df.to_csv('alv.csv')
#Step 1: Connect to MongoDB - Note: Change connection string as needed
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["finance"]
mycol = mydb["mycollection"]

# Step 3: Get data from DB
data_from_db = mycol.find_one({"index":"SPY"})
output_dataframe = pd.DataFrame(data_from_db["data"])
output_dataframe.set_index("Date",inplace=True)
print(output_dataframe)


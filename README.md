# News and trading
The main goal of of this project is to predict whether company stock will rise or fall the next day with time series algorithms and sentiment analysis of news articles

# Requirement
Keras
Pandas
numpy
scikit-learn
matplotlib

# Trading project

The main goal of our app is to predict if a stock price is about to increase or decrease on the following day. We will analyse the Dow Jones companies to analyze their stock patterns and give useful information to our application users. 

## Heroku Deployment

The application is available [here](https://trading-app-simplon.herokuapp.com/). 


## Data collection 

We used the AlphaVantage API to collect the time series (daily) of each stock. For company news, we used the Stock News API. Locally, the data has been stored in a **Postgresql** database but for deployment purposes, we imported all the information into a **SQLite** database. 

### Preprocessing

We did an Exploratory Data Analysis in the **data_wrangling/preparation_dataset.ipynb** notebook.
We used the **MSFT** stock to understand how to prepare the dataset for an LSTM model.

### Machine Learning

We compared a 1-hidden-layer LSTM and a 1-hidden-layer Bidirectional LSTM. We observed the results are slightly better with a simple LSTM so we trained and saved the simple model for each stock.


### Download project

```shell
git clone https://github.com/renatakaczor/Trading_project.git
cd trading-project
python -m venv venv/
source venv/Scripts/activate # Windows
source venv/bin/activate # Mac
pip install -r requirements.txt
```

### Database configuration (POSTGRESQL)
 
Before creating the tables needed for this project, you must create a posgresql database. Then, you can run the following command from the root of the project : 

```shell
psql -U user -h localhost -d db_name -f script.sql
```

It will create all the tables necessary for the project.


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

The application is available 

### Preprocessing

We did an Exploratory Data Analysis in the **serie.ipynb** notebook.


### Machine Learning

 We observed the results are slightly better with a simple LSTM so we trained and saved the simple model for each stock.


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


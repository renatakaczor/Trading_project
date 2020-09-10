import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
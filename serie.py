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
rolling = X.
rolling_mean
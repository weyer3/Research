import pandas as pd
url = 'https://raw.githubusercontent.com/weyer3/Research/master/11_13_19_Callibration.csv'
df = pd.read_csv(url)
df.head()

import matplotlib.pyplot as plt

plt.plot(df.iloc[:,0], df.iloc[:,1],df.iloc[:,2],df.iloc[:,3])
plt.show()
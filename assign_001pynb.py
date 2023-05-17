# -*- coding: utf-8 -*-
"""Assign 001pynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14PLDjdE0gFTS1HoAAkU_SdwccZ-l1P7h
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

df=pd.read_csv('/content/house price - DOC-20230516-WA0024..csv')
df.head()

sns.histplot(df.Date,kde=True)

# BIVARITE ANALYSIS

df[['id','Date','number of bedrooms','number of bathrooms','living area','lot area']].describe()

sns.scatterplot(df.id)
plt.ylim(0,15000)

sns.pairplot(df[['id','Date','number of bedrooms','number of bathrooms','living area','lot area']],hue='id')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv('/content/house price - DOC-20230516-WA0024..csv')
df

df.describe()

df.mean()

df.mode()

df.median()

df.info()

average = df['id'].mean()
print(average)
med = df['id'].median()
print(med)

norm_data = pd.DataFrame(np.random.normal(size=1000))
norm_data.plot(kind="density",figsize=(5,5));

plt.vlines(norm_data.mean(),
           ymin=0,
           ymax=0.4,
           linewidth=4.0);
plt.vlines(norm_data.median(),
          ymin=0,
          ymax=0.4,
          linewidth=2.0,
          color="red");

skewed_data = pd.DataFrame(np.random.exponential(size=10000))
skewed_data.plot(kind="density",figsize=(5,5),xlim=(-1,5));
plt.vlines(skewed_data.mean(),
           ymin=0,
           ymax=0.8,
           linewidth=4.0,
           color="black");
plt.vlines(skewed_data.median(),
          ymin=0,
          ymax=0.8,
          linewidth=2.0,
          color="red");

max(df["id"])-min(df["id"])

five_num = [df["id"].quantile(0),
            df["id"].quantile(0.25),
            df["id"].quantile(0.50),
            df["id"].quantile(0.75),
            df["id"].quantile(1)]
five_num

df["id"].describe()
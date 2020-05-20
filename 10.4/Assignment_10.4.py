import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'ah_item_small.csv').set_index('Unnamed: 0')

df.hist(column = 'bid', bins = 100)
df.hist(column = 'buyout', bins = 100)
df['equippable'].value_counts().plot(kind = 'bar')
df.hist(column = 'quality', bins = 4)
df.hist(column = 'requiredLevel', bins = 10)

bid = df['bid'].to_numpy()
print('Mean =', bid.mean(), 
      'Median =', bid.median(), 
      'SD =', bid.std(), 
      'Variance =', bid.var())

buyout = df['buyout']
print('Mean =', buyout.mean(), 
      'Median =', buyout.median(), 
      'SD =', buyout.std(), 
      'Variance =', buyout.var())

equip = df['equippable'].value_counts()
print(equip)

qual = df['quality'].value_counts()
print(qual)

reqLvl = df['requiredLevel'].value_counts()
reqLvl.head(5)

reqLvl.tail(5)
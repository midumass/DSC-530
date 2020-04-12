import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Temp\ah_item.csv').set_index('Unnamed: 0')
df2= df.sample(50000)

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
# Mean = 138118976.5507437 Median = 5999986.0 SD = 2100040098.820838 Variance = 4.4101684166554353e+18

buyout = df['buyout']
print('Mean =', buyout.mean(), 
      'Median =', buyout.median(), 
      'SD =', buyout.std(), 
      'Variance =', buyout.var())
# Mean = 143091809.92677325 Median = 6317765.0 SD = 2149187410.5249696 Variance = 4.619006525559024e+18

equip = df['equippable'].value_counts()
print(equip)
# False    3280270
# True     1819751

qual = df['quality'].value_counts()
print(qual)
# 1.0    1849505
# 2.0    1737504
# 3.0    1010492
# 4.0     491547
# 0.0       9742
# 5.0       1231

reqLvl = df['requiredLevel'].value_counts()
reqLvl.head(5)
# 0.0      2444458
# 120.0     338488
# 1.0       253446
# 100.0     214455
# 110.0     123592

reqLvl.tail(5)
# 4.0      1833
# 3.0      1435
# 2.0       865
# 105.0     569
# 115.0       2



n = hist.Total()
d = {}
for x, freq in hist.Items():
    d[x] = freq / n

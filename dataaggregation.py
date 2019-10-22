import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print (df)

r = df.rolling(window=3,min_periods=1)
print (r)

#by passing function
df2 = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df2)

r = df2.rolling(window=3,min_periods=1)
print (r.aggregate(np.sum))

#single row aggregation
df3 = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df3)
r = df3.rolling(window=3,min_periods=1)
print (r['A'].aggregate(np.sum))

#multiple column aggregation
df4 = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df4)
r = df4.rolling(window=3,min_periods=1)
print (r[['A','B']].aggregate(np.sum))
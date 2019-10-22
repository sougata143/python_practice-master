#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

#creating an empty panel
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)

df1 = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df1 = df1.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df1)
print(df1['one'].isnull())

df2 = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one',
'two', 'three'])
df2 = df2.reindex(['a', 'b', 'c'])
print(df2)
print ("NaN replaced with '0':") 
print(df2.fillna(0))
print("NaN replacing forwardfill or pad")
print(df2.fillna(method = 'pad'))
print("NaN replacing backfill or bill")
print(df2.fillna(method = 'bfill'))
print("excluding NaN")
print(df2.dropna())

df3 = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]})
print("Replace Missing (or) Generic Values")
print(df3.replace({1000:10,2000:60}))
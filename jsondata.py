import pandas as pd

data = pd.read_json('./input.json')
print (data)
# Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])

data2 = pd.read_json('path/input.xlsx')

print(data2.to_json(orient='records', lines=True))
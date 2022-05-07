import pandas as pd

df1 = pd.DataFrame({'name' : ['Kate', 'Ivan', 'Pavel', 'Igor'], 'rank': [1,2,3,4]})

df2 = pd.DataFrame({'name' : ['Kate', 'Ivan', 'Pavel', 'Igor'], 'rank': [3,1,4,2]})

print(pd.merge(df1, df2, on="name",suffixes=["_O", "_G"]))
import pandas as pd

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.count())

#print(df.groupby('TAG').sum())
#print(df.groupby('TAG').count())

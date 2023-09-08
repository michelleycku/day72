import pandas as pd

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
# print(df)
#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.count())

#print(df.groupby('TAG').sum())
#print(df.groupby('TAG').count())

## test dataframe for pivot
# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
#                         'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
#                         'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# print(test_df)
#
# pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)

## Can you pivot the df DataFrame so that each row is a date and each column is a programming language?
## Store the result under a variable called reshaped_df

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)

## We can also check if there are any NaN values left in the entire DataFrame with this line:
print(reshaped_df.isna().values.any())

# print(reshaped_df)
# print(reshaped_df.columns)
# print(reshaped_df.head())
# print(reshaped_df.tail())
# print(reshaped_df.count())



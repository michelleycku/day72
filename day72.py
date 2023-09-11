import pandas as pd
import matplotlib.pyplot as plt

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
# print(reshaped_df.shape())
# print(reshaped_df.columns)
# print(reshaped_df.head())
# print(reshaped_df.tail())
# print(reshaped_df.count())

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)

plt.show()
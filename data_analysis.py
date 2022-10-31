import pandas as pd
import numpy as np

url = 'data_analysis_file.csv'
df = pd.read_csv(url)
# df.to_csv("data_analysis_file.csv")
print(df.head(3))
print()

# reverse column
print(df.loc[:, ::-1].head(3))
print("reverse column")

print(df.dtypes)  # datatype
print("datatype")

print(df.shape)
print("shape")

print(df.isna().sum())  # null
print("null")

features_nan = [feature for feature in df.columns if df[feature].isna().sum() > 1 and df[feature].dtypes == 'O']

for feature in features_nan:
    print('{}:{}% missing values'.format(feature, np.round(df[feature].isna().mean(), 2)))
print()

print(df.loc[20:25], ["Genres", "Budget"])
print()

df.rename(columns={"Review Rating": "Review"}, inplace=True)  # rename column

print(df.Review.isin([4.6]).value_counts())  # counts of 4.6
print()

print(df.sort_values(by="Review", ascending=False).head(3))  # descending
print()

print(df[df.Language == "Hindi"].head(3))
print()

print(df.describe(percentiles=[.01, .02, .05, .09]).round(2))
print()

print(df.describe(include='O'))
print()

print(df.describe(include='all'))

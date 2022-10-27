import pandas as pd

df = pd.DataFrame({'name': ['Tom', 'Andy', 'Lucas'],
                   'DoB': ['08-05-1997', '04-28-1996', '12-16-1995']})
df['DoB'] = pd.to_datetime(df['DoB'])
df['year'] = df['DoB'].dt.year
df['month'] = df['DoB'].dt.month
df['day'] = df['DoB'].dt.day
print(df)

import pandas as pd

"""
dt.week, dt.dayofweek, and dt.is_leap_year are the inbuilt attributes to get the week of year, the day of week, 
and leap year.
"""

df = pd.DataFrame({'name': ['Tom', 'Andy', 'Lucas'],
                   'DoB': ['01-04-1997', '04-28-1996', '12-16-1995']})
df['DoB'] = pd.to_datetime(df['DoB'])
df['week_of_year'] = df['DoB'].dt.week
df['day_of_week'] = df['DoB'].dt.dayofweek
df['is_leap_year'] = df['DoB'].dt.is_leap_year
print(df)

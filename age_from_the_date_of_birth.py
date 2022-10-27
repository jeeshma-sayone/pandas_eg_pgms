import pandas as pd

"""
dt.week, dt.dayofweek, and dt.is_leap_year are the inbuilt attributes to get the week of year, the day of week,
and leap year.
"""

df = pd.DataFrame({'name': ['Tom', 'Andy', 'Lucas'],
                   'DoB': ['01-04-1997', '04-28-1996', '10-26-1995']})
df['DoB'] = pd.to_datetime(df['DoB'])

today = pd.to_datetime('today')
df['age'] = today.year - df['DoB'].dt.year
print(df)

"""
This is not accurate as people might haven't had their birthday this year. A more accurate solution would be to 
consider the birthday
"""

# Year difference
today = pd.to_datetime('today')
diff_y = today.year - df['DoB'].dt.year
# Haven't had birthday
b_md = df['DoB'].apply(lambda x: (x.month, x.day))
no_birthday = b_md > (today.month, today.day)
df['age'] = diff_y - no_birthday
print(df)

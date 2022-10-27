"""
Pandas to_datetime() is able to parse any valid date string to datetime without any additional arguments.
"""
import pandas as pd

df = pd.DataFrame({'date': ['3/10/2000', '3/11/2000', '3/12/2000'],
                   'value': [2, 3, 4]})
df['date'] = pd.to_datetime(df['date'])
print(df)
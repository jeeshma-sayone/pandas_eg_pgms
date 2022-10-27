import pandas as pd

"""
to_datetime() can be used to assemble a datetime from multiple columns as well. The keys (columns label) can be 
common abbreviations like [‘year’, ‘month’, ‘day’, ‘minute’, ‘second’, ‘ms’, ‘us’, ‘ns’]) or plurals of the same
"""

df = pd.DataFrame({'year': [2015, 2016],
                   'month': [2, 3],
                   'day': [4, 5]})
df['date'] = pd.to_datetime(df)
print(df)

import pandas as pd

"""
By default, to_datetime() will parse string with month first (MM/DD, MM DD, or MM-DD) format, and this arrangement is 
relatively unique in the United State.

In most of the rest of the world, the day is written first (DD/MM, DD MM, or DD-MM). If you would like Pandas to 
consider day first instead of month, you can set the argument dayfirst to True.
"""

df = pd.DataFrame({'date': ['3/10/2000', '3/11/2000', '3/12/2000'],
                   'value': [2, 3, 4]})
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
print(df)

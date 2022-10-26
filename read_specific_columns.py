import pandas as pd
cols = [1, 2, 3]
df = pd.read_excel('employee.xlsx', usecols=cols)
print(df)

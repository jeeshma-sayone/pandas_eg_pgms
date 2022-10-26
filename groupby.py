import pandas as pd

df = pd.read_excel('employee.xlsx')
df_sub = df[["emp_id", "salary"]].groupby('emp_id').sum()
print(df_sub)

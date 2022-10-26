import pandas as pd

df = pd.read_excel('employee.xlsx')
dt = df[df["emp_id"] == 119].head()
print(dt)

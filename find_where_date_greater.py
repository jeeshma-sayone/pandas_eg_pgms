import pandas as pd

df = pd.read_excel('employee.xlsx')
dt = df[df['hire_date'] >= '20220101']
print(dt)

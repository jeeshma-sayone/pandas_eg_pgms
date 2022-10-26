import pandas as pd

df = pd.read_excel('employee.xlsx')
dt = df[df["salary"] > 20000].head()
print(dt)

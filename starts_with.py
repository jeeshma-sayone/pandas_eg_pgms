import pandas as pd

df = pd.read_excel('employee.xlsx')
dt = df[df["first_name"].map(lambda x: x.startswith('J'))].head()
print(dt)

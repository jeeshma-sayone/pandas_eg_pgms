import pandas as pd

df = pd.read_excel('employee.xlsx')
dt = df.query('first_name == ["David", "Jose Manuel"]').head()
print(dt)

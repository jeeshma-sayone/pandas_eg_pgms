import pandas as pd

df = pd.read_excel('employee.xlsx')
result = df.sort_values('hire_date')
print(result)

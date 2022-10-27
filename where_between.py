import pandas as pd

df = pd.read_excel('employee.xlsx')
result = df[(df['hire_date'] >= 'Jan-2006') & (df['hire_date'] <= 'Dec-2023')]
print(result)



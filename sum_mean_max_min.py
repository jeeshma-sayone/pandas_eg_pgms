import pandas as pd

df = pd.read_excel('employee.xlsx')
print("Sum: ", df["salary"].sum())
print("Mean: ", df["salary"].mean())
print("Maximum: ", df["salary"].max())
print("Minimum: ", df["salary"].min())

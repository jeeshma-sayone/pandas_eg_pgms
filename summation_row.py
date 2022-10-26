import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')
sum_row = df[["Production", "Labor_Hours"]].sum()
df_sum = pd.DataFrame(data=sum_row).T
df_sum = df_sum.reindex(columns=df.columns)
print(df_sum)
# print("Sum: ", df["Production"].sum())
# print("Sum: ", df["Labor_Hours"].sum())

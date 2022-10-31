import pandas as pd

df = pd.DataFrame(zip(range(1, 11), "ABcdxABcdX"), columns=['num', 'letter'])
print(df, end='\n\n')

groups = {
    'A': 'upper',
    'B': 'upper',
    'c': 'lower',
    'd': 'lower'
}

df['group'] = df.apply(lambda row: groups.get(row['letter'], 'unknown'), axis=1)
print(df)
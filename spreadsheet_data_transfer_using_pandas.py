'''
A program to transfer data from one file to another and also update it with names absent
'''

import pandas as pd
import numpy as np

# files to be transferred
cols = ['Name', 'Age', 'Sex']
s0 = pd.Series(['Cent', 23, 'M'])
s1 = pd.Series(['Ben', 24, 'M',])
s2 = pd.Series(['Kate', 28, 'F'])
s3 = pd.Series(['Ryan', 43, 'M'])
s4 = pd.Series(['Bob', 19, 'M'])
s5 = pd.Series(['Reynolds', 31, 'M'])
s6 = pd.Series(['Kelly', 30, 'M'])

# transfer destination + updating
s7 = pd.Series(['Bob', '', '',])
s8 = pd.Series(['Kate', '', ''])
s9 = pd.Series(['Ben', '', ''])
s10 = pd.Series(['Kelly', '', ''])

df1 = pd.DataFrame([list(s0), list(s1), list(s2), list(s3), list(s4), list(s5), list(s6)], columns = cols)
df2 = pd.DataFrame([list(s7), list(s8), list(s9), list(s10)], columns = cols)
df3 = pd.DataFrame(columns=cols)
print(' Data to be transferred: ')
print(df1)

print('\n', 'Transfer Destination:')
print(df2)

for name in df1['Name']:
    if name in df2['Name'].values:
        x = np.where(df1['Name'] == name)
        y = np.where(df2['Name'] == name)
        df2.loc[int(y[0]), 'Age'] = df1.loc[int(x[0]), 'Age']
        df2.loc[int(y[0]), 'Sex'] = df1.loc[int(x[0]), 'Sex']
    else:
        x = np.where(df1['Name'] == name)
        new_row = [name, df1.loc[int(x[0]), 'Age'], df1.loc[int(x[0]), 'Sex']]
        df3 = pd.DataFrame(np.insert(df3.values, 0, new_row, axis=0), columns=cols)

print('\n', 'Data to be updated:')
print(df3)

df2 = pd.concat([df2, df3], ignore_index=True)
print('\n', 'New Datasheet:')
print(df2)


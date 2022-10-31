# now let us first take the desired modules

import numpy as np
import pandas as pd

# so we have imported two libraries

# time to make the DataFrame now

players = [['M.S.Dhoni', 36, 75], ['A.B.D. Villiars', np.nan, 74], ['V.kholi', 31, np.nan], ['S.smith', 34, np.nan]]

df = pd.DataFrame(players, columns=['Names', 'Age', 'Weights'])

print(df)

# Let us now check the null values in the parted sum

print(df.isnull().sum())

df1 = df.dropna()
print(df1)

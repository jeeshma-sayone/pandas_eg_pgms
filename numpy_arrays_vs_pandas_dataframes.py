import numpy as np
import pandas as pd

# >>>Inicial data in list format

heights_arr = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183,
               180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188,
               182, 185, 191]

ages_arr = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51,
            56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

# >>>Creating 1darrays

heights_arr_np = np.array(heights_arr).reshape((-1, 1))
heights_arr_short = heights_arr_np[:5]

# reshape((-1,1)) transposes a row vector to a column vector while reshape((1,-1)) tranposes a column vector to a row vector

ages_arr_np = np.array(ages_arr).reshape((-1, 1))
ages_arr_short = ages_arr_np[:5]

print("This is a numpy 1darray")
print(heights_arr_short)
print('\n')

# >>>Creating one-dimensional dataframes

heights_arr_pd = pd.DataFrame({'heights': heights_arr}).head()

ages_arr_pd = pd.DataFrame({'ages': ages_arr}).head()

print(
    'And this is its corresponding one-column pandas dataframe (the advantage is that you can label each column with a title)')
print(heights_arr_pd)
print('\n')

# >>>Joining the two np 1darrays in a 2darray

height_age_arr = np.hstack((heights_arr_short, ages_arr_short))

print('This is a numpy 2darray')
print(height_age_arr)
print('\n')

# >>>Creating a two column dataframe from the initial lists

height_age_arr_pd = pd.DataFrame({
    'heights': heights_arr,
    'ages': ages_arr
})
height_age_arr_pd = height_age_arr_pd.head()

print('And this is a two-column data frame created from the initial lists')
print(height_age_arr_pd)
print('\n')

print('Which also works taking the two one-column dataframes previosly created and concatenating them')
height_age_arr_pd2 = pd.concat([heights_arr_pd, ages_arr_pd], axis=1)
print(height_age_arr_pd2)
print('\n')

# >>>Calculating the column sum in each case

print('Column sum for the numpy 2darray')
print(height_age_arr.sum(axis=0))
print('\n')

print('Column sum for the two-column dataframe')
print(height_age_arr_pd.sum())

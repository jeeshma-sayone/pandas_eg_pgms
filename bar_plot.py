import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('employee.xlsx')
sorted_by_production = df.sort_values(['salary'], ascending=False).head(10)
sorted_by_production['salary'].head(10).plot(kind="barh")
plt.show()

import pandas as pd
import numpy as np
data = np.array([5, 10, 15, 20, 25])
s = pd.Series(data)
print(s)
print("Convert Pandas Series to Python list", s.tolist())


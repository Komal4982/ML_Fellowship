import pandas as pd
x = pd.Series([0, 1, 2, 3, 4, 5, 6])
print("Original array")
print(x)
power = x * x *x
print("First array elements raised to powers from second array, element-wise:""\n", power)
print(power.tolist())


# import numpy as np
# x = np.arange(7)
# print(x)
# print(np.power(x, 3))


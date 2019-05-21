import numpy as np
x = np.zeros(10)
print(x)
x.flags.writeable = False
print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
x[0] = 1

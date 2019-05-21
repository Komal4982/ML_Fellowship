import numpy as np
Array1 = [0, 10, 20, 40, 60, 80]
Array2 = [10, 30, 40, 50, 70, 90]
print(Array1, Array2)
x = np.setdiff1d(Array1, Array2)
print("Set difference between two arrays:=", x)
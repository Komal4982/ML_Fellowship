import numpy as np
Array1 = [0, 10, 20, 40, 60]
Array2 = [10, 30, 40]
X = np.intersect1d(Array1, Array2)
print("common element into two arrays:=", X)

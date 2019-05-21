import numpy as np
array = [[0, 1, 2, 3],
         [4, 5, 6, 7],
         [8, 9, 10, 11]]
print(array)


array = np.arange(12).reshape(3, 4)
print("Original array elements:")
print(array)


for x in np.nditer(array, op_flags=['readwrite']):
    x[...] = 3 * x

print("multi:\n", array)





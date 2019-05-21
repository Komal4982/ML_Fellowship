import numpy as np
Original_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(Original_array)
index = [0, 3, 4]
new_array = np.delete(Original_array, index)
print(new_array)

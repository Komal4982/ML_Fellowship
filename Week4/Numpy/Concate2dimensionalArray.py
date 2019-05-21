import numpy as np
sample_list = np.array([[0, 1, 3], [5, 7, 9]])
sample_list1 = np.array([[0, 2, 4], [6, 8, 10]])
x = np.concatenate((sample_list, sample_list1), 1)
print(x)
























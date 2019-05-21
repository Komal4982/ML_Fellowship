import numpy as np


def get_pattern(matrix, row, col):
    # iterate over rows
    for r_count in range(0, row):
        # iterate over cols
        for c_count in range(0, col):
            # if row 1 or more and col less than row print 1
            if r_count > 0 and c_count < r_count:
                print("1", end=" ")
            else:
                print(matrix[r_count][c_count], end=" ")
                # print zero's as it is
        print()


arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
r = 4
c = 3
# function call to get above pattern
get_pattern(arr, r, c)

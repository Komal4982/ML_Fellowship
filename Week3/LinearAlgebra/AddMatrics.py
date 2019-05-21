
def add_matrix(x, y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    return result


matrix_1 = [[12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[5, 8, 1],
            [6, 7, 3],
            [4, 5, 9]]

Mat = add_matrix(matrix_1, matrix_2)

for m in range(len(Mat)):
    print(Mat[m])
print("\n")

#
# n = 3
# m = 3
# val = [1] * n
# for x in range(n):
#     val[x] = [2] * m
# print(val)

def matrix_mul(X, Y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(X[0])):
            for k in range(len(X)):
                result[i][j] += X[i][k] * Y[k][j]
    return result




matrix_1 = [[12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[5, 8, 1],
            [6, 7, 3],
            [4, 5, 9]]


Mat = matrix_mul(matrix_1, matrix_2)
for M in range(len(Mat)):
    print(Mat[M])

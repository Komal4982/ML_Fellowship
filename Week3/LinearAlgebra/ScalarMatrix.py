def scalar_mul(row, num):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(row)):
        for j in range(len(row[0])):
            result[i][j] = row[i][j] * num
    return result


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = 9

scalar_matrix = scalar_mul(X, Y)
for m in range(len(scalar_matrix)):
    print(scalar_matrix[m])
# print(m)


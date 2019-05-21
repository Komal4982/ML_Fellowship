Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]



result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]



def transpose_matrix(matrix):
    # iterate through rows
    for i in range(len(matrix)):
        # iterate through column
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]


transpose_matrix(Y)
for r in result:
    print(r)


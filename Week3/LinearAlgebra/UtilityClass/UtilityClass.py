class Utility:
    # .............determinant matrix..............

    def Determinant_matrix(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        return (matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[2][1] * matrix[1][2]))
                - matrix[1][0] * ((matrix[0][1] * matrix[2][2]) - (matrix[2][1] * matrix[0][2]))
                + matrix[2][0] * ((matrix[0][1] * matrix[1][2]) - (matrix[0][2] * matrix[1][1])))
# transpose of matrix

    def transpose_matrix(self, matrix_1):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for row in range(len(matrix_1)):
            for col in range(len(matrix_1[0])):
                result[col][row] = matrix_1[row][col]
        return result


# vector multiplication matrix


    def MulVectorMatrix(self, X, Y):
        result = [0] * len(X)
        sum1 = 0
        for i in range(len(X)):
            r = X[i]
        # iterate through columns of Y
            for j in range(len(Y)):
                sum1 += sum(r[j] * Y[j])
                result[i] = sum1
            sum1 = 0
        return result

    def get_matrix_minor(self, m,  i, j):
        return [row[:j] + row[j + 1:]for row in (m[:i] + m[i + 1:])]


    def get_inverse_matrix(self, m):
        determinant = self.Determinant_matrix(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of co_factors
        co_factors = []
        for r in range(len(m)):
            co_factor_row = []
            for c in range(len(m)):
                minor = self.get_matrix_minor(m, r, c)
                co_factor_row.append(((-1) ** (r + c)) * self.Determinant_matrix(minor))
            co_factors.append(co_factor_row)
        co_factors = self.transpose_matrix(co_factors)
        for r in range(len(co_factors)):
            for c in range(len(co_factors)):
                co_factors[r][c] = co_factors[r][c] / determinant
        return co_factors


    def ace_cards_display(self, total_no_ace_cards, total_cards):
        probability = total_no_ace_cards / total_cards
        return probability





    def onehead(self, coin_toss):
        oneH = 0
        for item in coin_toss:
            cnt = 0
            for char in item:
                if char == 'H':
                    cnt += 1

            if cnt == 1:
                oneH += 1
        return oneH

     # Find two Head
    def FindTwoHead(self, coin_toss):
        twoHead = 0
        for item in coin_toss:
            cnt = 0
            for char in item:
                if char == 'H':
                    cnt += 1

            if cnt >= 2:
                twoHead += 1
        return twoHead

    def AtleastOneHead(self, coin_toss):
        oneH = 0
        for item in coin_toss:
            cnt = 0
            for char in item:
                if char == 'H':
                    cnt += 1

            if cnt >= 1:
                oneH += 1
        return oneH
#  probability of drawing an ace after drawing a king on the first draw


    def calProbability(self, possibilities, totaloutcome):
        return round((possibilities / totaloutcome), 2)


# Get the probability that there are more than 120 errors in a certain data packet

    @staticmethod
    def probability_data_packet(data_mean, standard_deviation,  bit_error, bit_packet):
        z_score = (bit_packet - data_mean) / (standard_deviation * (bit_error ** 0.5))
        return z_score

    @staticmethod
    def probability_customer(mean, standard_deviation, cust_num1, cust_num2, cust_num3):

        z_score1 = (cust_num2 - mean * cust_num1) / (standard_deviation * (cust_num1 ** 0.5))

        z_score2 = (cust_num3 - mean * cust_num1) / (standard_deviation * (cust_num1 ** 0.5))

        return z_score1, z_score2

    @staticmethod
    # get the total probability of patients
    def prescribed_pain_pills(event1, event2, event3, event4):
        total_probability = event1 * event2 + event3 * event4

    # probability of pain pills for patients to be prescribed
        probability = (event1 * event2) / total_probability

        return probability

from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class InverseMatrix:
    def __init__(self):
        self.util = Utility()

    x = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    def inverse_matrix(self):
        try:
            print("Original Matrix : ")
            for v in range(len(self.x)):
                print(self.x[v])
        # getting inverse of matrix
            c = self.util.get_inverse_matrix(self.x)
            print("Inverse of matrix : ")
            for value in range(len(c)):
                print(c[value])
        except Exception as e:
            print(e)


# instantiation
InverseMatrix_object = InverseMatrix()
InverseMatrix_object.inverse_matrix()




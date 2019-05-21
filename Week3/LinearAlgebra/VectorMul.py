from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class VectorMul:
    def __init__(self):
        self.util = Utility()

        self.X = [[5, 1, 3], [1, 1, 1], [1, 2, 1]],
        self.Y = [1, 2, 3]



    def CreateMatrix(self):
        # calling vector matrix multiplication method by passing parent class variables using Utility class object
        vectorMatrix = self.util.MulVectorMatrix(self.X, self.Y)
        # calling display method by using class object  
        vector_obj.display(vectorMatrix)

    def display(self, vectorMatrix):
        # printing matrix X
        print(" Matrix X")
        for item in self.X:
            print(item)

        # printing matrix Y
        print("\nVector Y")
        for item in self.Y:
            print(item)

        # printing vector matrix multiplication of matrix
        print("\nVector matrix multiplication is :")
        print(vectorMatrix)


# creating object of class
vector_obj = VectorMul()
# calling method by using class object
vector_obj.CreateMatrix()

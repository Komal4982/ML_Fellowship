from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class CorrelationCoefficient:
    def __init__(self):
        self.sample_list1 = [68, 72, 65, 70, 62, 75, 78, 64, 68]
        self.sample_list2 = [90, 85, 88, 100, 105, 98, 70, 65, 72]

    def findsum(self):
        lengthX = len(self.sample_list1)
        print("length of X:=", lengthX)
        lengthY = len(self.sample_list2)
        print("length of Y:=", lengthY)

        sumx = 0
        sumy = 0

        for item in self.sample_list1:
            sumx = sumx + item
        print("sum of X is:=", sumx)

        for item in self.sample_list2:
            sumy = sumy + item
        print("sum of Y is:=", sumy)


        sumationX = sumx / lengthX
        sumationY = sumy / lengthY
        print("sumation of X is:=", sumationX)
        print("sumation of Y is :=", sumationY)



        # def findXY(sumationX, sumationY):
        #     CorrelationResult = (sumationX * sumationY) / 3 ** (sumationX**2 * sumationY**2)
        # print(CorrelationResult)
        #
        #
        # coefficient_obj.findXY()


coefficient_obj = CorrelationCoefficient()
coefficient_obj.findsum()



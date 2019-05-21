from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class Mammogram:
    def __init__(self):
        self.util = Utility()

    # One percent of women have breast cancer
        self.A = 0.01

    # 99% women don't have cancer
        self.probComplimentary = 0.99

    #  Ninety percent of women who have breast cancer test positive on mammograms.
        self.X = 0.90

    # Eight percent of women will have false positives.
        self.X1Complimentary = 0.08


    def calProbability(self):
        print("we assume ; \n Event A = women has cancer \n Event X = she has positive mammograms")
        print("\n One percent of women over 50 have breast cancer that is P(A):=", self.A)

        print("\n", self.probComplimentary, "don't have cancer that is P(~A):=", self.probComplimentary)

        print("\n Ninety percent of women who have breast cancer test positive on mammograms,P(X|A)):=", self.X)

        print("\n Eight percent of women will have false positives that is P(X|~A):=", self.X1Complimentary)

        probability = ((self.X * self.A) / (self.X * self.A) +
                       (self.X1Complimentary * self.probComplimentary))
        print("Probability:=", probability)


mammogram_obj = Mammogram()
mammogram_obj.calProbability()

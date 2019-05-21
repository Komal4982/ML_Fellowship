import random


class Random:
    def __init__(self):
        self.rangediff = 6
        self.possibility = 1

    def generateNum(self):
        num = random.randint(2, 7)
        print("random no is:=", num)
        print("Probability of getting a random number", num, ":=", round(self.possibility / self.rangediff), 2)


obj_random = Random()
obj_random.generateNum()

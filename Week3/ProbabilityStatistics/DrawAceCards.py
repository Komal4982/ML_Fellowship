from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class Probability:
    def __init__(self):
        self.util = Utility

    total_cards = 52
    total_no_ace_cards = 4

    def display_ace(self):
        prob = self.util.calProbability(self, self.total_no_ace_cards, self.total_cards)
        print(round(prob, 2))



obj = Probability()
obj.display_ace()

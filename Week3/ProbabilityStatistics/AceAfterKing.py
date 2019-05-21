from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class AceAfterKing:
    def __init__(self):
        self.util = Utility

    # total cards
    cards = 52
    print(cards)

    # total no of ace in pack of cards
    ace = 4
    print(ace)

    # remaining cards after drawing a king
    cards = cards - 1
    print("after drawing a king", cards)

    # creating utility class object
    Utility_obj = Utility()

    def findprobability(self):
        probability = self.util.calProbability(self, self.ace, self.cards)
        print(probability)

        print("\n probability of drawing an ace after drawing a kong on the first draw",
              self.ace, self.cards, "=", probability)


obj = AceAfterKing()
obj.findprobability()






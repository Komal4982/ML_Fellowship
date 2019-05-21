from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class TossCoin:
    def __init__(self):
        self.util = Utility()

        self.coin_toss = ['HHH', 'HHT', 'HTH', 'HTT', 'THT', 'THH', 'TTH', 'TTT']
        self.count = len(self.coin_toss)
        print(self.coin_toss)
        print(self.count)

    # probability of three heads, HHH

    def probabilty_coin(self):
        possibilities = self.coin_toss.count('HHH')
        print(possibilities)

        probability = self.util.calProbability(possibilities, self.count)
        print("\n probability of three heads is", possibilities, "/", self.count, "=", probability)


    # probability that you observe exactly one heads


    def FindOneHead(self):
        oneHead = self.util.onehead(self.coin_toss)
        print(oneHead)
        probability = self.util.calProbability(oneHead, self.count)
        print(probability)

    # observed at least one heads
    def FindTwoHead(self):
        AtLeastOnehead = self.util.AtleastOneHead(self.coin_toss)
        print(AtLeastOnehead)
        probability1 = self.util.FindTwoHead(self.coin_toss)
        print("\n print probability that you observe at least one head is",  self.count, "=", probability1)



    # observe at least two heads
        twoHead = self.util.FindTwoHead(self.coin_toss)
        print(twoHead)
        probability2 = self.util.calProbability(twoHead, self.count)
        print(probability2)

        print("probability of A2/A1=", (probability2 / probability1))





    def menu(self):
        print("\n 1.the probability of three heads")
        print("\n 2.the probability that you observe exactly one heads")
        print("\n 3.the possibility that you observe at least two heads")
        print("\n 0.exit")

        flag = False
        while flag == False:
            try:
                choice = int(input("Enter the choice"))
                if choice >= 0 and choice <= 3:
                    if choice == 1:
                        obj_coin.probabilty_coin()
                    if choice == 2:
                        obj_coin.FindOneHead()
                    if choice == 3:
                        obj_coin.FindTwoHead()
                    if choice == 0:
                        exit()
                        flag = True
                else:
                    raise ValueError
            except ValueError:
                print("\n please enter valid input")

        # flag = False
        #
        # while flag == False:
        #     try:
        #         choice = int(input("Enter your choice"))
        #         if choice >= 0 and choice <= 3:
        #             if choice == 1:
        #                 obj_coin.probabilty_coin()
        #                 flag = True
        #                 if flag == True:
        #                     pass
        #
        #                     # self.menu()
        #
        #             if choice == 2:
        #                 obj_coin.FindOneHead()
        #
        #             if choice == 3:
        #                 obj_coin.FindTwoHead()
        #
        #             if choice == 0:
        #                 flag = True
        #
        #         else:
        #             raise ValueError
        #     except ValueError:
        #         print("\n please give valid input")
        #         print("Try again")



obj_coin = TossCoin()
flag = False
obj_coin.menu()

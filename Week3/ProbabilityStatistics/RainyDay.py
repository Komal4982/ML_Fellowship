class RainyDay:
    def __init__(self):
        self.rainy = 1 / 3
        self.rainy_traffic = 1 / 2
        self.rainy_traffic_late = 1 / 2
        self.rainy_traffic_notLate = 1 / 2

        self.rainy_notTraffic = 1 / 2
        self.rainy_notTraffic_late = 1 / 4
        self.rainy_notTraffic_notLate = 3 / 4

        self.notRainy = 2 / 3
        self.notRainy_Traffic = 1 / 4
        self.notRainy_Traffic_late = 1 / 4
        self.notRainy_Traffic_notLate = 3 / 4



        self.notRainy_notTraffic = 3 / 4
        self.notRainy_notTraffic_late = 1 / 8
        self.notRainy_notTraffic_notLate = 7 / 8

    def traffic(self):
        print((self.notRainy) * (self.notRainy_Traffic) * (self.notRainy_Traffic_notLate))

    def notRainy_Traffic_notLate(self):
        print("hello")
        # print("the probability that it's not raining and there is heavy traffic and I am not late:=",
        #       self.notRainy * self.notRainy_Traffic * self.notRainy_Traffic_notLate)


    def late(self):
        print("the probability that I am late:=", self.rainy * self.rainy_traffic * self.rainy_traffic_late)


    def late_rainy(self):
        print("i am late,rainy, traffic then probability:=", self.rainy * self.rainy_traffic * self.rainy_traffic_late)
        print(" I arrived late at work, what is the probability that it rained that day:=",
         self.rainy * self.rainy_traffic * self.rainy_traffic_late + self.rainy * self.rainy_notTraffic * self.rainy_notTraffic_late)




    def menu(self):
        print("\n 1.What is the probability that it's not raining and there is heavy traffic and I am not late")
        print("\n 2.What is the probability that I am late")
        print("\n 3.Given that I arrived late at work, what is the probability that it rained that day")
        print("\n 0.exit")
        flag = False
        while flag == False:
            try:
                choice = int(input("Enter the choice"))
                if choice >= 0 and choice <= 3:
                    if choice == 1:
                        rainy_obj.traffic()
                    if choice == 2:
                        rainy_obj.late()
                    if choice == 3:
                        rainy_obj.late_rainy()
                    if choice == 0:
                        exit()
                        flag = True
                else:
                    raise ValueError
            except ValueError:
                print("\n please enter valid input")


rainy_obj = RainyDay()
flag = False
rainy_obj.menu()

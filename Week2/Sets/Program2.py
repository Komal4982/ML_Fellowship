from utility.UtilityClass import Utility


class Iterate:
    def __init__(self):
        self.util = Utility()


    def iterate_num(self):
        num_set = set([0, 1, 2, 3, 4, 5])
        self.util.iterate_set(num_set)
        # print(iterate_new_set)


iter_obj = Iterate()
iter_obj.iterate_num()


# .........................or..................

def iterate_num(num_set):
    for n in num_set:
        print(n)


num_set = set([0, 1, 2, 3, 4, 5])
iterate_num(num_set)


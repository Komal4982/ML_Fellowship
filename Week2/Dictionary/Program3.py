from utility.UtilityClass import Utility


class Dictionary:
    def __init__(self):
        self.util = Utility()

    def Concate_Dictionary(self):
        d1 = {1: 10, 2: 20}
        d2 = {3: 30, 4: 40}
        d3 = {5: 50, 6: 60}
        d4 = {}
        concate_new_dict = self.util.concate_dict(d1, d2, d3, d4)
        print(concate_new_dict)


dict_obj = Dictionary()
dict_obj.Concate_Dictionary()

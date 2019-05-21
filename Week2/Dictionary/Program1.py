class Dictionary:
    s_dict = 0

    def __init__(self):
        self.dict = {1: 20, 8: 70, 5: 30}


    def sort_dict(self, dict_1):
        self.s_dict = sorted(dict_1.values())
        r_sort = sorted(dict_1.values(), reverse=True)
        print(self.s_dict, r_sort)


obj = Dictionary()
obj.sort_dict(obj.dict)



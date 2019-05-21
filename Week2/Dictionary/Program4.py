from utility.UtilityClass import Utility


class Iterate:
    def __init__(self):
        self.util = Utility()

    def display_dict(self):

        d = {'Black': 1, 'Yellow': 2, 'Orange': 3}
        self.util.iterate_dict(d)


obj = Iterate()
obj.display_dict()


from utility.UtilityClass import Utility


class RemoveSet:
    def __init__(self):
        self.util = Utility()

    def rm_set(self):
        day = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
        print(day)
        items = input("which item you want to remove")
        i = self.util.validate(items)
        if i:
            print("Please enter string")
        else:
            remove = self.util.remove(day, items)
            print("Set:", remove)


remove_obj = RemoveSet()
remove_obj.rm_set()





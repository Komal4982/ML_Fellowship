from utility.UtilityClass import Utility


class Unique:
    def __init__(self):
        self.util = Utility()

    def unique(self):
        sample_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
        print("original list:", sample_dict)


        while 1:
            try:
                print("1.Find unique values in dictionary\n2.Display Original Dictionary\n3.Exit")
                ch = input("Enter your choice")
                choice = self.util.validate(ch)  # call to object of util class with its methods cll

                if choice:
                    ch = int(ch)  # conversion string to int

                    if ch == 1:
                        unique_data = self.util.unique_val(sample_dict)
                        print(unique_data)
                    elif ch == 2:
                        print("Original Dictionary:", sample_dict)
                    elif ch == 3:
                        exit()
                    else:
                        print("Enter choice b/w 1-3")
                else:
                    print("please enter valid choice")
            except Exception as e:
                print(e)


Unique_obj = Unique()
Unique_obj.unique()







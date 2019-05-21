# .......................Dictionary.........................



class Utility:

    def __init__(self):
        self.n = 10

    # ................Range.................................
    def loop(self):
        for i in range(0, self.n):
            print("loop:", i)

# ..................Iterate Dictionary.....................
    def iterate_dict(self, d):
        for color_key, value in d.items():
            print(color_key, 'corresponds to ', d[color_key])

# .................Concatenate Dictionary...................
    def concate_dict(self, d1, d2, d3, d4):
        for d in (d1, d2, d3):
            d4.update(d)
        return d4

# ....................Unique Dictionary.....................
    def unique_val(self, L):
        unique_value = set(val for uniq in L for val in uniq.values())
        return list(unique_value)
        # print("Unique Values: ", unique_value)


    def validate(self, n):
         try:
             int(n)
             return True
         except Exception:
             return False
# ........................Iterate in set...............


    def iterate_set(self, num_set):
        for n in list(num_set):
            print(n)

# ..................Remove Items ...........

    def remove(self, day, items):
        if items not in day:
            print("Not found")
        else:
            new_list = []
            for d in day:
                if items != d:
                    new_list.append(d)
            return set(new_list)




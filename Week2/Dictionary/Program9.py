
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}



def printer(list_obj):
    a, b, c = list_obj
    print(a, ' ', b, ' ', c)



printer(my_dict.keys())

for i in range(0, len(my_dict['C1'])):
    a = list()
    for keys in my_dict.keys():
        a.append(my_dict[keys][i])
    printer(a)


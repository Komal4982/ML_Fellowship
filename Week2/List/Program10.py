
def enumerte_fun(Sample_List):
    l = []
    for i in range(len(Sample_List)):
        if i not in [0, 4, 5]:
            l.append(Sample_List[i])
    return l


Sample_List = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
print("Original List:", Sample_List)
list1 = enumerte_fun(Sample_List)
print(list1)










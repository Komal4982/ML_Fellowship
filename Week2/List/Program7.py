def cloning(list1):
    list1_copy = list1[:]
    return list1_copy



list1 = [9, 8, 5, 2, 4]
list2 = cloning(list1)
print("original list:", list1)
print("After cloning:", list2)



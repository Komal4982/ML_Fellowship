def convert(list1):
    return tuple(list1)


list_items = ["red", "blue", "black", "green"]
del list_items[0]

print("items are in list:", list_items)


print("items are converted into list to tuple:", convert(list_items))


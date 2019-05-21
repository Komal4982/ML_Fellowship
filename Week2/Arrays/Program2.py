def Reverse(array_items):
    rev = []
    for items in array_items[::-1]:
        rev.append(items)
    return rev


array_items = [5, 9, 10, 8, 6]
# print("Reverse array:", array_items[::-1])
print(Reverse(array_items))








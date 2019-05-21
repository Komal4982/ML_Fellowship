
def concatenate_list(list_temp):
    result = ' '
    for l in list_temp:

        result += str(l)

    return result





element1 = input('Enter the element 1:')
element2 = input('Enter the element 2: ')
element3 = input('Enter the element 3: ')
element4 = input('Enter the element 4: ')
List = [element1, element2, element3, element4]

print("the list element are:", List)

print("List element return in string is:", concatenate_list(List))


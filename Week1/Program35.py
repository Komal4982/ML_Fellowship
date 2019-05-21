
while True:
    try:
        ele1 = input("Enter the element1:")
        ele2 = input("Enter the element2:")
        ele3 = input("Enter the element3:")
        ele1 = int(ele1)
        ele2 = int(ele2)
        ele3 = int(ele3)
        List = [ele1, ele2, ele3]
        print('Your List is: ' + str(List))

        new_list = list(filter(lambda x: (x % 15 == 0), List))
        print("number is divided by 15:=", new_list)
        break
    except ValueError:
        print('Please enter a integer number')









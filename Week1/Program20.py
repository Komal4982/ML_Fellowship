
try:
    a = int(input("Enter the number1:"))
    b = int(input("Enter the number2:"))
    c = int(input("Enter the number3:"))

    x = min(a, b, c)
    z = max(a, b, c)
    y = (a + b + c) - x - z

    print("Numbers in sorted order: ", x, y, z)


except Exception as e:
    print("please enter integer number", e)



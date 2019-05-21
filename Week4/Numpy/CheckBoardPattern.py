import numpy as np


def checkboardpattern(n):
   print("Checkerboard pattern:")
   x = np.zeros((8, 8), dtype=int)
   x[1::2, ::2] = 1
   x[::2, 1::2] = 1
   for i in range(number):
      for j in range(number):
         print(x[i][j], end=" ")
      print()


number = int(input("Enter value of number:="))
checkboardpattern(number)

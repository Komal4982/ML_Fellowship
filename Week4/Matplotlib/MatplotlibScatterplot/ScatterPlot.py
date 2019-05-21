import matplotlib.pyplot as plt
from pylab import randn
import numpy as np
import math
import random





class ScatterPlot:
    def __init__(self):


        print("1.Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted"
              " against each other")
        print("2.Write a Python program to draw a scatter plot with empty circles taking a random distribution in X and"
              " Y and plotted against each other.")
        print("3.Write a Python program to draw a scatter plot using random distributions to generate balls of"
              " different sizes.")
        print("4.Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science."
              " Use marks of 10 students")
        print("5.Write a Python program to draw a scatter plot for three different groups camparing weights and heights")

    def display_plot(self):

        flag = True

        while flag:

            try:
                print()
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:

                    """Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted
                     against each other"""


                    X = randn(200)
                    Y = randn(200)
                    plt.scatter(X, Y, color='r')
                    plt.xlabel("X")
                    plt.ylabel("Y")
                    plt.show()

                elif choice == 2:

                    """Write a Python program to draw a scatter plot with empty circles taking a random distribution in 
                    X and Y and plotted against each other."""

                    x = np.random.randn(50)
                    y = np.random.randn(50)
                    plt.scatter(x, y, s=70, facecolors='none', edgecolors='g')
                    plt.xlabel("X")
                    plt.ylabel("Y")
                    plt.show()

                elif choice == 3:

                    """Write a Python program to draw a scatter plot using random distributions to generate balls of 
                    different sizes. """


                    # create random data
                    no_of_balls = 25
                    x = [random.triangular() for i in range(no_of_balls)]
                    y = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
                    colors = [random.randint(1, 4) for i in range(no_of_balls)]
                    areas = [math.pi * random.randint(5, 15) ** 2 for i in range(no_of_balls)]
                    # draw the plot
                    plt.figure()
                    plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
                    plt.axis([0.0, 1.0, 0.0, 1.0])
                    plt.xlabel("X")
                    plt.ylabel("Y")
                    plt.show()

                elif choice == 4:

                    """Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and 
                    Science. Use marks of 10 students"""


                    math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
                    science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
                    marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                    plt.scatter(marks_range, math_marks, label='Math marks', color='r')
                    plt.scatter(marks_range, science_marks, label='Science marks', color='g')
                    plt.title('Scatter Plot')
                    plt.xlabel('Marks Range')
                    plt.ylabel('Marks Scored')
                    plt.legend()
                    plt.show()

                elif choice == 5:
                    """Write a Python program to draw a scatter plot for three different groups camparing weights and
                     heights. """

                    weight1 = [67, 57.2, 59.6, 59.64, 55.8, 61.2, 60.45, 61, 56.23, 56]
                    height1 = [101.7, 197.6, 98.3, 125.1, 113.7, 157.7, 136, 148.9, 125.3, 114.9]
                    weight2 = [61.9, 64, 62.1, 64.2, 62.3, 65.4, 62.4, 61.4, 62.5, 63.6]
                    height2 = [152.8, 155.3, 135.1, 125.2, 151.3, 135, 182.2, 195.9, 165.1, 125.1]
                    weight3 = [68.2, 67.2, 68.4, 68.7, 71, 71.3, 70.8, 70, 71.1, 71.7]
                    height3 = [165.8, 170.9, 192.8, 135.4, 161.4, 136.1, 167.1, 235.1, 181.1, 177.3]
                    weight = np.concatenate((weight1, weight2, weight3))
                    height = np.concatenate((height1, height2, height3))
                    plt.scatter(weight, height, marker='*')
                    plt.xlabel("weight", fontsize=16)
                    plt.ylabel("height", fontsize=16)
                    plt.title("Group wise weight and height scatter plot", fontsize=20)
                    plt.show()


                else:
                    print("\n Enter Valid choice between 0-10")


            except Exception as e:
                print(e)
                print("Invalid input")


scatter_obj = ScatterPlot()
scatter_obj.display_plot()

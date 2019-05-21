import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import randn
import seaborn as sb
# import this for hover effect
import mplcursors


class Plotly:
    def __init__(self):
        print("1. Write a program to draw a scatter plot for random 1000 x and y coordinates")
        print("2. Write a program to draw line and scatter plots for random 100 x and y coordinates")
        print("3. Write a program to draw a scatter plot for random 500 x and y coordinates and style it")
        print("4. Write a program to draw a scatter plot for a given dataset and show datalabels on hover")


    def while_display(self):

        flag = True

        while flag:

            try:
                print()
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:
                    print("\n Enter how many random values you want for scatter plot, on x and y axis")
                    x_axis = int(input("X axis values"))
                    y_axis = int(input("Y axis values"))
                    X = randn(x_axis)
                    Y = randn(y_axis)
                    """ 
                    Cartesian coordinates to display values for typically two variables for a set of data (x, y).
                    If the points are color-coded, one additional variable can be displayed (color = 'r')"""
                    plt.scatter(X, Y, color='r')
                    plt.xlabel("X axis")
                    plt.ylabel("Y axis")
                    plt.title("Scatter Plot with random number")
                    plt.show()



                elif choice == 2:
                    print("\n Enter how many random values you want for scatter plot, on x and y axis")
                    x_axis = int(input("X axis values"))
                    y_axis = int(input("Y axis values"))
                    X = randn(x_axis)
                    Y = randn(y_axis)

                    # it shows lines for random X and Y values
                    plt.scatter(X, Y, color='b')
                    plt.plot(X, Y)
                    plt.xlabel('X Axis')
                    plt.ylabel('Y Axis')
                    plt.title("Lines with scatter plot")
                    plt.show()

                elif choice == 3:
                    print("\n Enter how many random values you want for scatter plot, on x and y axis")
                    x_y_axis = int(input("X axis values"))
                    x_y_axis = int(input("Y axis values"))
                    X = randn(x_y_axis)
                    Y = randn(x_y_axis)

                    x = np.random.rand(x_y_axis)
                    y = np.random.rand(x_y_axis)
                    colors = np.random.rand(x_y_axis)
                    area = (30 * np.random.rand(x_y_axis)) ** 2
                    # 0 to 15 point radii
                    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
                    # show color scale
                    plt.colorbar()
                    plt.title("Scatter plot with style")
                    plt.show()

                elif choice == 4:
                    # read data from given csv file
                    df = pd.read_csv("states.csv")
                    print(len(df))
                    sb.scatterplot(data=df, x='Rank', y='Population')
                    # used to show hover effect,
                    # When hover is set to True, annotations are displayed when the mouse hovers over the point
                    mplcursors.cursor(hover=True)
                    plt.title("Scatter plot for a given dataset and with hover")
                    plt.show()

                else:
                    print("enter choice between 0 to 4")
            except Exception as e:
                print(e)


util_obj = Plotly()
util_obj.while_display()

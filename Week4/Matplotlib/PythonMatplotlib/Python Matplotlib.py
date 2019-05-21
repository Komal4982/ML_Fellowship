import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import datetime as DT
from matplotlib.dates import date2num






class MatPlotLib:
    def __init__(self):





        print("1.Write a Python program to draw a line with suitable label in the x axis, y axis and a title")
        print("2.Write a Python program to draw a line using given axis values with suitable label in the x axis , "
              "y axis and a title")
        print("3.Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, "
              "2016 to October 7, 2016. ")
        print("4.Write a Python program to plot two or more lines on same plot with suitable legends of each line.")
        print("5.Write a Python program to plot two or more lines with legends, different widths and colors")
        print("6.Write a Python program to plot two or more lines with different styles")
        print("7.Write a Python program to plot two or more lines and set the line markers.")
        print("8.Write a Python program to display the current axis limits values and set new axis values")
        print("9.Write a Python program to plot quantities which have an x and y position")
        print("10.Write a Python program to plot several lines with different format styles in one command using arrays")
        print("11.Write a Python program to create multiple types of charts")
        print("12.Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc."
              "between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and "
              "color blue.Date,Close")
        print("13.Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc."
              " between October 3, 2016 to October 7, 2016. Customized the grid lines with rendering with a larger grid"
              "(major grid) and a smaller grid (minor grid).Turn on the grid but turn off ticks. ")
        print("14.Write a Python program to create multiple plots. ")

    def while_display(self):

        flag = True

        while flag:

            try:
                print()
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:
                    """1.Write a Python program to draw a line with suitable label in the x axis, y axis and a title"""
                    X = range(1, 50)
                    Y = [value * 3 for value in X]
                    print(Y)
                    print("Values of X:")
                    print(*range(1, 50))
                    print("Values of Y (thrice of X):")
                    print(Y)
                    # Plot lines and/or markers to the Axes.
                    plt.plot(X, Y)
                    # Set the x axis label of the current axis.
                    plt.xlabel('X - axis')
                    # Set the y axis label of the current axis.
                    plt.ylabel('Y - axis')
                    # Set a title
                    plt.title('Draw a line.')
                    # Display the figure.
                    plt.show()

                elif choice == 2:
                    """Write a Python program to draw a line using given axis values with suitable label in the x axis , 
                    y axis and a title"""
                    # x axis values
                    x = [1, 2, 3]
                    # y axis values
                    y = [2, 4, 1]
                    # Plot lines and/or markers to the Axes.
                    plt.plot(x, y)
                    # Set the x axis label of the current axis.
                    plt.xlabel('x - axis')
                    # Set the y axis label of the current axis.
                    plt.ylabel('y - axis')
                    # Set a title
                    plt.title('Sample graph!')
                    # Display a figure.
                    plt.show()

                elif choice == 3:

                    """Write a Python program to draw line charts of the financial data of Alphabet Inc. between October
                     3, 2016 to October 7, 2016."""


                    df = pd.read_csv('fdata.csv')
                    df.plot()
                    plt.show()

                elif choice == 4:

                    """ Write a Python program to plot two or more lines on same plot with suitable legends of each 
                    line"""


                    # line 1 points
                    x1 = [10, 20, 30]
                    y1 = [20, 40, 10]
                    # plotting the line 1 points
                    plt.plot(x1, y1, label="line 1")
                    # line 2 points
                    x2 = [10, 20, 30]
                    y2 = [40, 10, 30]
                    # plotting the line 2 points
                    plt.plot(x2, y2, label="line 2")
                    plt.xlabel('x - axis')
                    # Set the y axis label of the current axis.
                    plt.ylabel('y - axis')
                    # Set a title of the current axes.
                    plt.title('Two or more lines on same plot with suitable legends ')
                    # show a legend on the plot
                    plt.legend()
                    # Display a figure.
                    plt.show()

                elif choice == 5:

                    """Write a Python program to plot two or more lines with legends, different widths and colors"""


                    # line 1 points
                    x1 = [10, 20, 30]
                    y1 = [20, 40, 10]
                    # line 2 points
                    x2 = [10, 20, 30]
                    y2 = [40, 10, 30]
                    # Set the x axis label of the current axis.
                    plt.xlabel('x - axis')
                    # Set the y axis label of the current axis.
                    plt.ylabel('y - axis')
                    # Set a title
                    plt.title('Two or more lines with different widths and colors with suitable legends ')
                    # Display the figure.
                    plt.plot(x1, y1, color='blue', linewidth=3, label='line1-width-3')
                    plt.plot(x2, y2, color='red', linewidth=5, label='line2-width-5')
                    # show a legend on the plot
                    plt.legend()
                    plt.show()

                elif choice == 6:
                    """Write a Python program to plot two or more lines with different styles"""
                    # line 1 points
                    x1 = [10, 20, 30]
                    y1 = [20, 40, 10]
                    # line 2 points
                    x2 = [10, 20, 30]
                    y2 = [40, 10, 30]
                    # Set the x axis label of the current axis.
                    plt.xlabel('x - axis')
                    # Set the y axis label of the current axis.
                    plt.ylabel('y - axis')
                    # Plot lines and/or markers to the Axes.
                    plt.plot(x1, y1, color='blue', linewidth=3, label='line1-dotted', linestyle='dotted')
                    plt.plot(x2, y2, color='red', linewidth=5, label='line2-dashed', linestyle='dashed')
                    # Set a title
                    plt.title("Plot with two or more lines with different styles")
                    # show a legend on the plot
                    plt.legend()
                    # function to show the plot
                    plt.show()

                elif choice == 7:
                    """Write a Python program to plot two or more lines and set the line markers."""


                    # x axis values
                    x = [1, 4, 5, 6, 7]
                    # y axis values
                    y = [2, 6, 3, 6, 3]

                    # plotting the points
                    plt.plot(x, y, color='red', linestyle='dashdot', linewidth=3,
                             marker='.', markerfacecolor='blue', markersize=12)
                    # Set the y-limits of the current axes.
                    plt.ylim(1, 8)
                    # Set the x-limits of the current axes.
                    plt.xlim(1, 8)

                    # naming the x axis
                    plt.xlabel('x - axis')
                    # naming the y axis
                    plt.ylabel('y - axis')

                    # giving a title to my graph
                    plt.title('Display marker')
                    # function to show the plot
                    plt.show()

                elif choice == 8:
                    """Write a Python program to display the current axis limits values and set new axis values"""

                    X = range(1, 50)
                    Y = [value * 3 for value in X]
                    plt.plot(X, Y)
                    plt.xlabel('x - axis')
                    plt.ylabel('y - axis')
                    plt.title('Draw a line.')
                    # shows the current axis limits values
                    print(plt.axis())
                    # set new axes limits
                    # Limit of x axis 0 to 100
                    # Limit of y axis 0 to 200
                    plt.axis([0, 100, 0, 200])
                    # Display the figure.
                    plt.show()

                elif choice == 9:
                    """Write a Python program to plot quantities which have an x and y position"""
                    # Make an array of x values
                    x1 = [2, 3, 5, 6, 8]
                    # Make an array of y values for each x value
                    y1 = [1, 5, 10, 18, 20]
                    # Make an array of x values
                    x2 = [3, 4, 6, 7, 9]
                    # Make an array of y values for each x value
                    y2 = [2, 6, 11, 20, 22]
                    # set new axes limits
                    pl.axis([0, 10, 0, 30])
                    # use pylab to plot x and y as red circles
                    pl.plot(x1, y1, 'b*', x2, y2, 'ro')
                    # show the plot on the screen
                    pl.show()

                elif choice == 10:
                    """Write a Python program to plot several lines with different format styles in one command using 
                    arrays."""

                    # Sampled time at 200ms intervals
                    t = np.arange(0., 5., 0.2)

                    # green dashes, blue squares and red triangles
                    plt.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^')
                    plt.show()

                elif choice == 11:
                    """Write a Python program to create multiple types of charts"""


                    data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
                            (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
                            (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
                            (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
                            (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]

                    x = [date2num(date) for (date, value) in data]
                    y = [value for (date, value) in data]

                    fig = plt.figure()

                    graph = fig.add_subplot(111)

                    # Plot the data as a red line with round markers
                    graph.plot(x, y, 'r-o')

                    # Set the xtick locations
                    graph.set_xticks(x)

                    # Set the xtick labels
                    graph.set_xticklabels(
                        [date.strftime("%Y-%m-%d") for (date, value) in data]
                    )
                    plt.show()

                elif choice == 12:

                    """Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
                    Date,Close"""

                    data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
                            (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
                            (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
                            (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
                            (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]

                    x = [date2num(date) for (date, value) in data]
                    y = [value for (date, value) in data]

                    fig = plt.figure()

                    graph = fig.add_subplot(111)

                    # Plot the data as a red line with round markers
                    graph.plot(x, y, 'r-o')

                    # Set the xtick locations
                    graph.set_xticks(x)

                    # Set the xtick labels
                    graph.set_xticklabels(
                        [date.strftime("%Y-%m-%d") for (date, value) in data]
                    )

                    # naming the x axis
                    plt.xlabel('Date')
                    # naming the y axis
                    plt.ylabel('Closing Value')
                    # giving a title
                    plt.title('Closing stock value of Alphabet Inc.')
                    # Customize the grid
                    plt.grid(linestyle='-', linewidth='0.5', color='blue')
                    plt.show()

                elif choice == 13:
                    """Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc.
                     between October 3, 2016 to October 7, 2016. Customized the grid lines with rendering with a larger grid 
                     (major grid) and a smaller grid (minor grid).Turn on the grid but turn off ticks"""


                    data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
                            (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
                            (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
                            (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
                            (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]

                    x = [date2num(date) for (date, value) in data]
                    y = [value for (date, value) in data]

                    fig = plt.figure()

                    graph = fig.add_subplot(111)

                    # Plot the data as a red line with round markers
                    graph.plot(x, y, 'r-o')

                    # Set the xtick locations
                    graph.set_xticks(x)

                    # Set the xtick labels
                    graph.set_xticklabels(
                        [date.strftime("%Y-%m-%d") for (date, value) in data]
                    )

                    # naming the x axis
                    plt.xlabel('Date')
                    # naming the y axis
                    plt.ylabel('Closing Value')
                    # giving a title
                    plt.title('Closing stock value of Alphabet Inc.')
                    # Turn on the minor TICKS, which are required for the minor GRID
                    plt.minorticks_on()

                    # Customize the major grid
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

                    # Turn off the display of all ticks.
                    plt.tick_params(which='both',  # Options for both major and minor ticks
                                    top='off',  # turn off top ticks
                                    left='off',  # turn off left ticks
                                    right='off',  # turn off right ticks
                                    bottom='off')  # turn off bottom ticks
                    plt.show()

                elif choice == 14:

                    """Write a Python program to create multiple plots. """

                    fig = plt.figure()
                    fig.subplots_adjust(bottom=0.020, left=0.020, top=0.900, right=0.800)

                    plt.subplot(2, 1, 1)
                    plt.xticks(()), plt.yticks(())

                    plt.subplot(2, 3, 4)
                    plt.xticks(())
                    plt.yticks(())

                    plt.subplot(2, 3, 5)
                    plt.xticks(())
                    plt.yticks(())

                    plt.subplot(2, 3, 6)
                    plt.xticks(())
                    plt.yticks(())

                    plt.show()

                else:
                    print("\n Enter Valid choice between 0-14")


            except Exception as e:
                print(e)
                print("Invalid input")




plotlib_obj = MatPlotLib()
plotlib_obj.while_display()










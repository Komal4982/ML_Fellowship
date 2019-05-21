import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np
import matplotlib.patches as mpatches



class BarChart:
    def __init__(self):
        print("1. Write a Python programming to display a bar chart of the popularity of programming Languages. ")
        print("2. Write a Python programming to display a horizontal bar chart of the popularity of programming"
              " Languages")
        print("3. Write a Python programming to display a bar chart of the popularity of programming Languages. "
              "Use uniform color. ")
        print("4. Write a Python programming to display a bar chart of the popularity of programming Languages. "
              "Use different color for each bar. ")
        print("5. Write a Python programming to display a bar chart of the popularity of programming Languages. "
              "Attach a text label above each bar displaying its")
        print("6.Write a Python programming to display a bar chart of the popularity of programming Languages."
              " Make blue border to each bar. ")
        print("7. Write a Python programming to display a bar chart of the popularity of programming Languages. "
              "Specify the position of each bar plot. ")
        print("8. Write a Python programming to display a bar chart of the popularity of programming Languages."
              " Select the width of each bar and their positions.")
        print("9.Write a Python programming to display a bar chart of the popularity of programming Languages."
              "Increase bottom margin")
        print("10.Write a Python program to create bar plot of scores by group and gender. Use multiple X values on"
              " the same chart for men and women.")
        print("11.Write a Python program to create bar plot from a DataFrame.")
        print("12.Write a Python program to create bar plots with error bars on the same figure")
        print("13.Write a Python program to create bar plots with errorbars on the same figure. Attach a text label "
              "above each bar displaying men means (integer value).")






    def display_chart(self):

        flag = True

        while flag:

            try:
                print()
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:
                    """ Write a Python programming to display a bar chart of the popularity of programming Languages."""

                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]

                    plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.xticks(x_pos, x)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 2:
                    """Write a Python programming to display a horizontal bar chart of the popularity of programming 
                    Languages. """


                    x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]
                    print(x_pos)
                    plt.barh(x_pos, popularity, color='green')
                    plt.xlabel("Popularity")
                    plt.ylabel("Languages")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.yticks(x_pos, x)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 3:
                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]

                    plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))

                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.xticks(x_pos, x)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 4:
                    """Write a Python programming to display a bar chart of the popularity of programming Languages.
                     Use different color for each bar. """

                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]

                    plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.xticks(x_pos, x)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 5:
                    """Write a Python programming to display a bar chart of the popularity of programming Languages. 
                    Attach a text label above each bar displaying its"""

                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]

                    fig, ax = plt.subplots()
                    rects1 = ax.bar(x_pos, popularity, color='b')
                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.xticks(x_pos, x)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

                    def autolabel(rects):
                        """
                        Attach a text label above each bar displaying its height
                        """
                        for rect in rects:
                            height = rect.get_height()
                            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                    '%f' % float(height),
                                    ha='center', va='bottom')

                    autolabel(rects1)

                    plt.show()

                elif choice == 6:
                    """Write a Python programming to display a bar chart of the popularity of programming Languages.
                     Make blue border to each bar. """

                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]

                    plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.xticks(x_pos, x)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 7:
                    """Write a Python programming to display a bar chart of the popularity of programming Languages.
                     Specify the position of each bar plot. """

                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]
                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.xticks(x_pos, x)
                    # Select the position of each barplots on the x-axis (space=1,3,3,2,1)
                    y_pos = [0, 1, 4, 7, 9, 10]
                    # Create bars
                    plt.bar(y_pos, popularity)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 8:
                    """Write a Python programming to display a bar chart of the popularity of programming Languages. 
                    Select the width of each bar and their positions."""

                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]
                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    plt.xticks(x_pos, x)
                    # Select the width of each bar and their positions
                    width = [0.1, 0.2, 0.5, 1.1, 0.2, 0.3]
                    y_pos = [0, .8, 1.5, 3, 5, 6]

                    # Create bars
                    plt.bar(y_pos, popularity, width=width)
                    plt.xticks(y_pos, x)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 9:
                    """Write a Python programming to display a bar chart of the popularity of programming Languages. 
                    Increase bottom margin"""

                    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
                    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    x_pos = [i for i, _ in enumerate(x)]
                    plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))
                    plt.xlabel("Languages")
                    plt.ylabel("Popularity")
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
                    # Rotation of the bars names
                    plt.xticks(x_pos, x, rotation=90)
                    # Custom the subplot layout
                    plt.subplots_adjust(bottom=0.4, top=.8)
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                    # Customize the minor grid
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 10:
                    """Write a Python program to create bar plot of scores by group and gender. Use multiple X values
                     on the same chart for men and women."""

                    # data to plot
                    n_groups = 5
                    men_means = (22, 30, 33, 30, 26)
                    women_means = (25, 32, 30, 35, 29)

                    # create plot
                    fig, ax = plt.subplots()
                    index = np.arange(n_groups)
                    bar_width = 0.35
                    opacity = 0.8

                    rects1 = plt.bar(index, men_means, bar_width,
                                     alpha=opacity,
                                     color='g',
                                     label='Men')

                    rects2 = plt.bar(index + bar_width, women_means, bar_width,
                                     alpha=opacity,
                                     color='r',
                                     label='Women')

                    plt.xlabel('Person')
                    plt.ylabel('Scores')
                    plt.title('Scores by person')
                    plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
                    plt.legend()

                    plt.tight_layout()
                    plt.show()

                elif choice == 11:


                    a = np.array([[4, 8, 5, 7, 6], [2, 3, 4, 2, 6], [4, 7, 4, 7, 8], [2, 6, 4, 8, 6], [2, 4, 3, 3, 2]])
                    df = DataFrame(a, columns=['a', 'b', 'c', 'd', 'e'], index=[2, 4, 6, 8, 10])

                    df.plot(kind='bar')
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

                    plt.show()

                elif choice == 12:
                    """Write a Python program to create bar plots with error bars on the same figure"""

                    N = 5
                    menMeans = (54.74, 42.35, 67.37, 58.24, 30.25)
                    menStd = (4, 3, 4, 1, 5)
                    # the x locations for the groups
                    ind = np.arange(N)
                    # the width of the bars
                    width = 0.35
                    plt.bar(ind, menMeans, width, yerr=menStd, color='red')
                    plt.ylabel('Scores')
                    plt.xlabel('Velocity')
                    plt.title('Scores by Velocity')
                    # Turn on the grid
                    plt.minorticks_on()
                    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
                    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                    plt.show()

                elif choice == 13:
                    """Write a Python program to create bar plots with errorbars on the same figure. Attach a text 
                    label above each bar displaying men means (integer value)."""



                    N = 5
                    men_means = (54.74, 42.35, 67.37, 58.24, 30.25)
                    men_std = (4, 3, 4, 1, 5)

                    ind = np.arange(N)  # the x locations for the groups
                    width = 0.35  # the width of the bars

                    fig, ax = plt.subplots()
                    rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)

                    # add some text for labels, title and axes ticks
                    plt.ylabel('Scores')
                    plt.xlabel('Velocity')
                    plt.title('Scores by Velocity')

                    red_patch = mpatches.Patch(color='red', label='Men')
                    plt.legend(handles=[red_patch])

                    def autolabel(rects):
                        """
                        Attach a text label above each bar displaying its height
                        """
                        for rect in rects:
                            height = rect.get_height()
                            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                    '%d' % int(height),
                                    ha='center', va='bottom')

                    autolabel(rects1)
                    plt.show()
                else:
                    print("\n Enter Valid choice between 0-13")


            except Exception as e:
                print(e)
                print("Invalid input")



bar_obj = BarChart()
bar_obj.display_chart()
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from Week4.Seaborn.Utility.Util import Util


class SeabornPrograms:
    def __init__(self):
        self.utility = Util()

        print("1. Write a program to draw bar plot of sex against survived for a dataset given in the url ")
        print("2. Write a program to draw a point plot for sex against survived for a data set given in url ")
        print("3. program to draw a scatter plot of “day” against “total bill” for a data set given in a url.")
        print("4. Write a program to draw a violin plot of sex against total_bill  for a  given data set")
        print("5. program to draw a violin plot of “species” against “sepal length” for a data set given in a url")
        print("6. Write a program to draw a box plot of day by tips for a data set given in a url")
        print("7. Write a program to draw a swarm plot of total bill against size  for a  given data set.")
        print("8. Write a program to draw swarm plot of “total bill” against day for a data set given in url.")
        print("0. EXIT")


    def while_display(self):

            flag = True

            while flag:

                try:
                    print()
                    choice = int(input("Enter your choice"))

                    if choice == 0:
                        flag = False

                    elif choice == 1:

                        """Write a program to draw bar plot of sex against survived for a dataset given in the url"""

                        self.utility.Bar_plot()

                    elif choice == 2:

                        """Write a program to draw a point plot for sex against survived for a data set given in url"""

                        self.utility.Point_plot()

                    elif choice == 3:

                        """program to draw a scatter plot of “day” against “total bill” for a data set given in a url."""

                        self.utility.Scatter_plot()

                    elif choice == 4:

                        """4. Write a program to draw a violin plot of sex against total_bill  for a  given data set"""

                        self.utility.Violin_plots()

                    elif choice == 5:

                        """5. program to draw a violin plot of “species” against “sepal length” for a data set given in a url"""

                        self.utility.Violin_plots_species()



                    elif choice == 6:

                        """Write a program to draw a box plot of day by tips for a data set given in a url"""
                        self.utility.Box_plot_tips()


                    elif choice == 7:

                        """Write a program to draw a swarm plot of total bill against size  for a  given data set"""
                        self.utility.Swarm_plot()

                    elif choice == 8:

                        """Write a program to draw swarm plot of “total bill” against day for a data set given in url"""
                        self.utility.Swarm_plot_Day()

                    else:
                        print("\n Enter Valid choice between 0-8")


                except Exception as e:
                    print(e)
                    print("Invalid input")


# instantiation
plot_obj = SeabornPrograms()
plot_obj.while_display()





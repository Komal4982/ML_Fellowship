import matplotlib.pyplot as plt
import pandas as pd


class Piechart:
    def __init__(self):


        print("1. Write a Python programming to create a pie chart of the popularity of programming Languages.")
        print("2.Write a Python programming to create a pie chart with a title of the popularity of programming"
              " Languages. ")
        print("3.Write a Python programming to create a pie chart of gold medal achievements of five most "
              "successful countries in 2016 Summer Olympics. Read the data from a csv file. ")

    def while_display(self):

        flag = True

        while flag:

            try:
                print()
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:
                    # Data to plot
                    languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
                    popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
                    # explode 1st slice
                    explode = (0.1, 0, 0, 0, 0, 0)
                    # Plot

                    plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
                            autopct='%1.1f%%', shadow=True, startangle=140)

                    plt.axis('equal')
                    plt.show()

                elif choice == 2:

                    """Write a Python programming to create a pie chart with a title of the popularity of
                    programming Languages. """

                    # Plot data
                    languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
                    popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
                    # colors = ['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']
                    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
                    # explode 1st slice
                    explode = (0.1, 0, 0, 0, 0, 0)
                    # Plot
                    plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
                            autopct='%1.1f%%', shadow=True, startangle=140)
                    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago",
                              bbox={'facecolor': '0.8', 'pad': 5})
                    plt.show()

                elif choice == 3:
                    """Write a Python programming to create a pie chart of gold medal achievements of five most 
                    successful countries in 2016 Summer Olympics. Read the data from a csv file. """


                    df = pd.read_csv('medal.csv')
                    country_data = df["country"]
                    medal_data = df["gold_medal"]
                    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
                    explode = (0.1, 0, 0, 0, 0)
                    plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
                            autopct='%1.1f%%', shadow=True, startangle=140)
                    plt.title("Gold medal achievements of five most successful\n" + "countries in 2016 Summer Olympics")
                    plt.show()




                else:
                    print("\n Enter Valid choice between 0-3")


            except Exception as e:
                print(e)
                print("Invalid input")




pie_obj = Piechart()
pie_obj.while_display()

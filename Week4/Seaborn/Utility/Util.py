import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt


class Util:
    # "1. Write a program to draw bar plot of sex against survived for a dataset given in the url "


    def Bar_plot(self):
        df = sb.load_dataset('titanic')
        sb.barplot(x="sex", y="survived", hue="class", data=df)
        plt.title("Bar Plot")
        plt.show()


    # "2. Write a program to draw a point plot for sex against survived for a data set given in url "


    def Point_plot(self):
        df = sb.load_dataset('titanic')
        sb.pointplot(x="sex", y="survived", hue="class", data=df)
        plt.title("Point plot")
        plt.show()



    # 3. program to draw a scatter plot of “day” against “total bill” for a data set given in a url.


    def Scatter_plot(self):
        df_two = sb.load_dataset('tips')

    # create scatter plot with x and y axis
        sb.scatterplot(data=df_two, x="day", y="total_bill")

    # title for scatter plot
        plt.title("Scatter Plot")

    # show scatter plot
        plt.show()


    # "4. Write a program to draw a violin plot of sex against total_bill  for a  given data set")


    def Violin_plots(self):
        df = sb.load_dataset('tips')
        sb.violinplot(x="day", y="total_bill", data=df)
        plt.title("Violin plot")
        plt.show()

    # 5.Write a program to draw a violin plot of “species” against “sepal length” for a data set given in a url"
    def Violin_plots_species(self):
        df = sb.load_dataset('iris')
        sb.violinplot(x="species", y="sepal_length", data=df)
        plt.title("Violin Plot")
        plt.show()


     #  "6. Write a program to draw a box plot of day by tips for a dataset given in a url"

    def Box_plot_tips(self):
        # load required data set
        df_two = sb.load_dataset('tips')

        sb.boxplot(data=df_two, x="tip", y="day")
        plt.title("BOX PLOT")
        plt.show()

    # 7. Write a program to draw a swarm plot of total bill against size  for a  given dataset

    def Swarm_plot(self):
        # load required data set
        df = sb.load_dataset('tips')

        # create swarm plot with x and y axis
        sb.swarmplot(x="day", y="total_bill", data=df)

        # title for swarm plot
        plt.title("SWARM PLOT")

        # show swarm plot
        plt.show()

    # 8 Write a program to draw swarm plot of “total bill” against day for a dataset given in url
    def Swarm_plot_Day(self):
        df = sb.load_dataset('tips')
        sb.swarmplot(x="size", y="total_bill", data=df)
        plt.title("SWARM PLOT")
        plt.show()




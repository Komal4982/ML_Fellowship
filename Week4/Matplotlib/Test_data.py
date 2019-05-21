import matplotlib.pyplot as plt


class Test_data:
    def __init__(self):


        # def line_plotting(self):
        with open("text.txt") as f:
            # read content from file
            data = f.read()
        data = data.split('\n')
        # get row 0 value to x axis
        x = [row.split(' ')[0] for row in data]
        # get row 1 value to y axis
        y = [row.split(' ')[1] for row in data]
        # plot data in x y axes
        plt.plot(x, y)
        # set label for x axes
        plt.xlabel('x_axix')
        # set label for y axes
        plt.ylabel('y_axix')
        # title for plotting line
        plt.title('sample line')
        # show the figure
        plt.show()







test_obj = Test_data()




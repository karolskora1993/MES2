import matplotlib.pyplot as plt

class Plotter(object):
    @staticmethod
    def plot(xLabel, yLabel, xValues, yValues):
        fig = plt.gcf()
        fig.canvas.set_window_title('Wykres zależności temperatury od promienia')
        plt.title("Zależność temperatury od promienia")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.plot(xValues, [0 for i in range (0, len(xValues))])
        plt.show()
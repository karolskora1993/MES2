import matplotlib.pyplot as plt

class Plotter(object):
    @staticmethod
    def plot(xLabel, yLabel, xValues, yValues):
        fig = plt.gcf()
        fig.canvas.set_window_title('Wykres zależności temperatury od promienia')
        plt.title("Zależność temperatury od promienia")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        y1=[]
        y2=[]

        for i in range(0, len(yValues)):
            y1.append(yValues[i][0])
            y2.append(yValues[i][len(yValues[0])-1])

        plt.plot(xValues, y1, label="rMin")
        plt.plot(xValues, y2, label="rMax")
        plt.legend()
        plt.show()
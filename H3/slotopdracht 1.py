import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("H3\mjlo-15_0.txt", delimiter = ',')
day1 = data[:94]
day2 = data[94:]

def plot_figure(name, column):
    line_d1 = day1[:, column]
    line_d2 = day2[:, column]

    fig, ax = plt.subplots()
    ax.set_title(name)
    ax.set_xlabel("hour")
    ax.set_ylabel("value")
    ax.set_xlim(0, 24)
    ax.grid()

    time_d1 = np.linspace(0, 24, len(line_d1))
    time_d2 = np.linspace(0, 24, len(line_d2))
    ax.plot(time_d1, line_d1, label = "day1")
    ax.plot(time_d2, line_d2, label = "day2")

    ax.legend()
    plt.show(block = True)

plot_figure("voltage",1)
plot_figure("pressure",2)
plot_figure("lux",3)
plot_figure("uv",4)
plot_figure("voc",5)
plot_figure("humidity",6)
plot_figure("volume",7)
plot_figure("temperature",8)

import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('H3\mjlo-15_0.txt', delimiter = ',')
day1 = data[:94]
day2 = data[94:]

fig, ax = plt.subplots(4,2,figsize=(12,12))
fig.suptitle('Meetgegevens leefomgeving-kastje')

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.3,
                    hspace=0.8)

def plot_figure(name, column,i,j):
    line_d1 = day1[:, column]
    line_d2 = day2[:, column]

    time_d1 = np.linspace(0, 24, len(line_d1))
    time_d2 = np.linspace(0, 24, len(line_d2))
    ax[i,j].plot(time_d1, line_d1, label = 'day1',color='red')
    ax[i,j].plot(time_d2, line_d2, label = 'day2',color='green')

    ax[i,j].set_title(name)
    ax[i,j].set_xlabel('hour')
    ax[i,j].set_ylabel('value')
    ax[i,j].set_xlim(0, 24)
    ax[i,j].grid()
    ax[i,j].legend()

plot_figure('Voltage',1,0,0)
plot_figure('Pressure',2,0,1)
plot_figure('Lux',3,1,0)
plot_figure('Uv',4,1,1)
plot_figure('Voc',5,2,0)
plot_figure('Humidity',6,2,1)
plot_figure('Volume',7,3,0)
plot_figure('Temperature',8,3,1)

plt.show()
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("H3\mjlo-15_0.txt", delimiter = ',')

timestamp = data[:, 0]
voltage = data[:, 1]
pressure = data[:, 2]
lux = data[:, 3]
uv = data[:, 4]
voc = data[:, 5]
humidity = data[:, 6]
volume = data[:, 7]
temperature = data[:, 8]


plt.plot(timestamp)
plt.show()
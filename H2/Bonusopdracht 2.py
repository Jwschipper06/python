from tkinter import W
import numpy as np
np.set_printoptions(threshold = np.inf, linewidth = np.inf)
data = np.genfromtxt("bonus_getallen.txt", delimiter=',')
x = np.round(data)
x = x.astype(int)
x = str(x)
x = x.replace('[','')
x = x.replace(']','')
file = open("mooiecreatie.txt", "w")
file.write (x)
file.close

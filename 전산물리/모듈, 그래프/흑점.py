import numpy as np
import matplotlib.pyplot as plt

year, nspots, nd, n1, n2 = np.loadtxt('/Users/sungguchoi/Desktop/전산물리/모듈, 그래프/SN_y_tot_V2.0.csv', delimiter=';', unpack=True)
plt.plot(year, nspots)
plt.show()
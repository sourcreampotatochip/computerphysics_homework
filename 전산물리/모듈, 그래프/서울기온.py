import numpy as np
import matplotlib.pyplot as plt

locationnumber, location, date, avgtemp = np.loadtxt('/Users/sungguchoi/Desktop/전산물리/모듈, 그래프/OBS_ASOS_DD_20260922144459.csv', delimiter=',', unpack=True)
plt.plot(date, avgtemp)
plt.show()
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid

os.chdir(os.path.abspath(os.path.dirname(__file__)))

bins, count = [], []
with open("hist2.csv", "r") as f:
    for line in f.readlines():
        if line.strip():
            _b, _c = [float(i) for i in line.split(",")]
            bins.append(_b)
            count.append(_c)

x = np.array(bins)
y = np.array(count)

def gaussian(x, a, b, c):
    return a * np.exp(-((x - b) ** 2) / (2 * c ** 2))

def double_gaussian(x, a1, b1, c1, a2, b2, c2):
    return gaussian(x, a1, b1, c1) + gaussian(x, a2, b2, c2)

p0 = [1000, 0.9, 0.2, 500, 1.9, 0.5] 
popt, pcov = curve_fit(double_gaussian, x, y, p0=p0)

a1, b1, c1, a2, b2, c2 = popt

y_fit_total = double_gaussian(x, *popt)
y_fit_A = gaussian(x, a1, b1, c1)
y_fit_B = gaussian(x, a2, b2, c2)

area_A = trapezoid(y_fit_A, x)
area_B = trapezoid(y_fit_B, x)
ratio = area_A / area_B

print(f"입자 A 적분값: {area_A:.2f}")
print(f"입자 B 적분값: {area_B:.2f}")
print(f"두 입자의 생성비 (입자 A 적분값 / 입자 B 적분값): {ratio:.2f}")


bin_width = x[1] - x[0]
bin_edges = np.append(x-bin_width / 2, x[-1] + bin_width / 2)
n, bins, p = plt.hist(x, bins=bin_edges, weights=y, color='lightgray', alpha=0.6, label='Data')

plt.plot(x, y_fit_total, c='orangered', ls='-', label='A + B Fitting')
plt.plot(x, y_fit_A, c='royalblue', ls='--', label='A Fitting')
plt.plot(x, y_fit_B, c='deepskyblue', ls='-.', label='B Fitting')

plt.title('Data Fitting')
plt.xlabel('Energy')
plt.ylabel('Count')
plt.grid(True)
plt.legend()
plt.show()
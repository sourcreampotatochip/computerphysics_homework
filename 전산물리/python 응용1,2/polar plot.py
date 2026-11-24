import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0., np.pi*1,100)

f=lambda th: np.sin(th)*np.cos(th)
plt.polar(theta, f(theta), c='k')
plt.title('Polar Plot of sin(x)*cos(x)')
plt.show()
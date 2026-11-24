import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0, 5)
f= lambda x: np.cos(x)*np.cosh(x)-1
plt.plot(x, f(x), color = 'c', linestyle = '-.', linewidth='2.5')

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('plot of cos(x)*cosh(x)-1')
plt.show()
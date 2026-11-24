import matplotlib.pyplot as plt

def func(x):
    return np.sin(x)

plt.plot(x, func(x))
plt.grid(True)

plt.show()
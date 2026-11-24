import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

def g(func, x):
    y = []
    h = 0.01
    for _x in x:
        y.append((func(_x + h) - func(_x))/h)
    return np.array(y)

if __name__ == "__main__":
    x = np.linspace(0, 30, 500)
    plt.plot(x, f(x), label='sin(x)', color='black', ls='--')
    plt.plot(x, g(f, x), label='Derivative of sin(x)', color='red')
    plt.legend()
    plt.grid(True)
    plt.show()

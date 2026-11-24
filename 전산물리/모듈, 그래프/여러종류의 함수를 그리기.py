# y=3x+2 그래프 그리기
# 함수를 지정한 범위[0, 10]의 그래프로 

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x)

def func(x):
    return x

if __name__ == "__main__":
    x = np.linspace(0,10)
    y =3*x+2
    plt.plot(x,y)
    x= np.linspace(0, np.pi*3)
    plt.plot(x,func(x))
    plt.grid(True)
    plt.show()

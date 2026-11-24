import matplotlib.pyplot as plt
import numpy as np

from Trap1_function import trap1

def f(t):
    return t * np.cos(t)

# 적분 결과를 y에 저장합니다.
t, y = trap1(f, 0., np.pi/2)

# t에 대한 f(t)와 적분 값을 함께 플로팅합니다.
plt.plot(t, y, label='Integral of f(t)')
plt.plot(t, f(t), label='f(t)', linestyle='--')
plt.xlabel('t')
plt.ylabel('Value')
plt.title('Plot of f(t) and its integral over time')
plt.legend()
plt.grid()
plt.show()


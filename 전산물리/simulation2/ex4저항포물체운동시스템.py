import numpy as np
import matplotlib.pyplot as plt
from Euler_m_function import eulerm

g = 9.801 # m/s^2
m = 50/1000 # kg
cd = 4.3e-4 # kg/m

def f(t, yy):
    vx = yy[2]
    vy = yy[3]
    dy = np.zeros(4)
    dy[0] = vx
    dy[1] = vy
    dy[2] = - cd * vx * np.sqrt(vx**2)/2/m
    dy[3] = - g - cd * vy * np.sqrt(vx**2 + vy**2)/2/m
    return dy

t0 = 0
tf = 2.7 # sec
v0 = 67 # m/s
theta = 9 * np.pi/180 # radian
y0 = 10
yy0 = np.array([0, y0, v0 * np.cos(theta), v0 * np.sin(theta)])
h = 0.01
t, y = eulerm(f, yy0, t0, tf, h)
xp = y[:,0]

yp = np.tan(theta) * xp - g /2 /v0**2/ np.cos(theta)**2 * xp**2 + y0
plt.plot(y[:, 0], y[:, 1], c='k', label='drag')
plt.plot(xp, yp, c='k', ls='--', label = 'no drag')
plt.grid()
plt.title('2D tragectory')
plt.xlabel('range - m')
plt.ylabel('elevation - m')
plt.legend()
plt.show()
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]

with open("input.csv", "r") as f:
    for line in f.readlines():
        _x, _y = [float(i) for i in line.split(" ")]
        x.append(_x)
        y.append(_y)
    
coefficients = np.polyfit(x, y, 2) # 2는 다항식의 차수를 의미 (2차 다항식))
poly_eq = np.poly1d(coefficients) # 다항식을 생성

# 피팅된 함수에 따라 y값을 계산
y_fit = poly_eq(x)

# 원래 데이터와 피팅된 함수를 그래프로 표현
plt.scatter(x,y,label='Original Data', color='blue') # 원본 데이터 (산점도)
plt.plot(x, y_fit, label='Fitted Polynomial', color='red') # 피팅된 다항식

# 그래프 꾸미기
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(f'Polynomial Fit (Degree: 2)\nEquation: {coefficients[0]:.2f}x^2 + {coefficients[1]:.2f}x + {coefficients[2]:.2f}')
plt.grid(True)

#그래프 출력
plt.show()

degs = [1, 2, 3, 4, 5, 8, 14, 18]
new_x = np.linspace(0, 1)
plt.figure(figsize=(8, 10))
for idx, deg in enumerate(degs):
    # 계수 연산
    coef = np.polyfit(x, y, deg)
    # 연산한 계수를 함수로 만듦
    fit = np.poly1d(coef)
    # R^2값 계산
    sst = np.sum(np.power(y - np.average(y),2))
    ssr = np.sum(np.power(y - fit(x), 2))
    sqr = 1 - (ssr / sst)
    print(f"======= DEG: {deg}, R^2:{sqr:.3f} =======")
    print(coef)

    # 서브플롯 명령
    ax = plt.subplot(4, 2, idx +1)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1, 1)
    ax.text(0.05, -0.9, f"DEG: {deg}, $R^2$:{sqr:.3f}", fontsize=10)
    ax.plot(x, y, ".k")
    ax.plot(new_x, fit(new_x), "--r", label="DEG: {}".format(deg))
plt.savefig("01_data_fitting.png", bbox_inches="tight")
plt.show()
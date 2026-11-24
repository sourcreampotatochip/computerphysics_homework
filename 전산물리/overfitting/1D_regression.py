# Graph 상에 임의로 Dot을 찍어서 차수에 따른 그래프 변화를 확인한다
# 데이터와 1차(선형) 회귀

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1, 11).reshape(10, 1)
y = np.array([7, 8, 7, 13, 16, 15, 19, 23, 18, 21]).reshape(10, 1)

plt.plot(X, y, 'ro') # bo = blue + circle / use go (green cicle)

axes = plt.gca() # 현재 figure의 축을 가져옴
axes.set_ylim([0, 30])

plt.show()


reg = LinearRegression()
reg.fit(X,y)

w0 = reg.intercept_
w1 = reg.coef_

print('w0: ', w0)
print('w1: ', w1)

y_pred = reg.predict(X)

plt.plot(X, y, 'ro')
plt.plot(X, y_pred)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()

# 2차원 그래프, 2차(Quadratic) 다항 회귀
# np_c => 1차원 배열 두개를 col 방향으로 나열해서 concatenation
X_2 = np.c_[X, X**2] # 다항 회귀(polynomial regression)에서 기존 입력값 x에 "제곱항"을 추가
print(X_2)

reg = LinearRegression()
reg.fit(X_2, y)

w0 = reg.intercept_
w = reg.coef_

print('w0: ', w0)
print('w1: ', w[0][0])
print('w2: ', w[0][1])

print(reg.coef_)

y_pred_2 = reg.predict(X_2)

plt.plot(X, y, 'ro')
plt.plot(X_2[:,0], y_pred_2)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()

# 3차원 그래프, 3차(Cubic) 다항 회귀 - PolynomialFeatures 사용
# np_c => 1차원 배열 두개를 col 방향으로 나열해서 concatenation
X_3 = np.c_[X, X**2, X**3]
print(X_3)

from sklearn.preprocessing import PolynomialFeatures

polynomial = PolynomialFeatures(degree = 3, include_bias = False)
X_3_poly = polynomial.fit_transform(X)

reg = LinearRegression()
reg.fit(X_3_poly, y)

w0 = reg.intercept_
w = reg.coef_

print(w)

print('w0: ', w0)
print('w1: ', w[0][0]) # <- x^1에 곱해지는 w1
print('w2: ', w[0][1]) # <- x^2에 곱해지는 w2
print('w3: ', w[0][2]) # <- x^3에 곱해지는 w3

x_2 = np.array([2, 4, 8])
print(x_2)

y_2 = (np.array([2, 4, 8]) @ w.reshape(-1,1)) + w0
print(y_2)

print(w[0][2] * 8 + w[0][1] * 4 + w[0][0] * + 7.2)

y_pred_3 = reg.predict(X_3_poly) # X_3_poly @ w.reshape(-1,1)) + w0


plt.plot(X, y, 'ro')
plt.plot(X, y_pred_3)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()

X_new = np.arange(-5, 15, 0.01).reshape(-1, 1)

from sklearn.preprocessing import PolynomialFeatures

polynomial = PolynomialFeatures(degree = 3, include_bias = False)
X_new_3 = polynomial.fit_transform(X_new)

y_pred_3 = (X_new_3 @ w.reshape(-1, 1)) + w0

plt.plot(X_new, y_pred_3)

plt.plot(X, y, 'ro')
plt.plot(X_new, y_pred_3)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()

# 7차원 그래프 overfitting 시연
polynomial = PolynomialFeatures(degree = 7, include_bias = False)
X_7 = polynomial.fit_transform(X)
print(X_7)

reg = LinearRegression(tol=1e-15)
reg.fit(X_7, y)

w0 = reg.intercept_
w = reg.coef_

print(w,"\n")

print('w0: ', w0)
print('w1: ', w[0][0]) # <- x^1에 곱해지는 w1
print('w2: ', w[0][1]) # <- x^2에 곱해지는 w2
print('w3: ', w[0][2]) # <- x^3에 곱해지는 w3
print('w4: ', w[0][3]) # <- x^1에 곱해지는 w1
print('w5: ', w[0][4]) # <- x^2에 곱해지는 w2
print('w6: ', w[0][5]) # <- x^3에 곱해지는 w3
print('w7: ', w[0][6]) # <- x^3에 곱해지는 w3

# x = 2 일때의 값을 구해보자
y_2 = (np.array([2,4,8,16,32,64,128]) @ w.reshape(-1,1)) + w0
print(y_2)

print(w[0][6] * 128 + w[0][5] * 64 + w[0][4] * 32 + w[0][3] * 16 + w[0][2] * 8 + w[0][1] * 4 + w[0][1] * 2 + w0)

# coef_.reshape를 알아볼 수 있게 다시 표현
print(["{:0.3f}".format(x) for x in reg.coef_.reshape(-1,)])

# w 값이 기형적으로 변하는 것을 볼 수 있다.

# w와 intercept 값을 이용해서 그래프를 새로 그려보자
# 그래프를 그릴 y 값 구하기
y_7 = (X_7 @ w.reshape(-1, 1)) + w0

plt.plot(X, y, 'ro')
plt.plot(X, y_7)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()

# x 값의 범위를 좁게해서 그래프를 연결되게 그려보자
X_new = np.arange(1, 10.5, 0.01).reshape(-1,1)

polynomial = PolynomialFeatures(degree =7, include_bias = False)
X_new_7 = polynomial.fit_transform(X_new)

# 그래프를 그릴 y 값 구하기
y_7_new = (X_new_7 @ reg.coef_.reshape(-1, 1)) + reg.intercept_

plt.plot(X, y, 'ro')
plt.plot(X_new, y_7_new)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()



# Ridege method로 overfitting 완화
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0) #수업에서는 람다

ridge.fit(X_7, y)
y_pred_ridge = ridge.predict(X_7)

w0 = ridge.intercept_
# w = ridge.coef_
w0 = ridge.coef_.reshape(1, -1) # 아래 w를 2D로 일관성을 맞추려면 reshape를 해야함
# reshape (1, -1) 1 : 행(row) 수를 1로 고정, -1 : 열(column) 수는 "자동 계산"
print(w, "\n")

print('w0: ', w0)
print('w1: ', w[0][0]) # <- x^1에 곱해지는 w1
print('w2: ', w[0][1]) # <- x^2에 곱해지는 w2
print('w3: ', w[0][2]) # <- x^3에 곱해지는 w3
print('w4: ', w[0][3]) # <- x^1에 곱해지는 w1
print('w5: ', w[0][4]) # <- x^2에 곱해지는 w2
print('w6: ', w[0][5]) # <- x^3에 곱해지는 w3
print('w7: ', w[0][6]) # <- x^3에 곱해지는 w3

# coef_.reshape를 알아볼 수 있게 다시 표현
print(["{:0.3f}".format(x) for x in w.reshape(-1,)])

# 그래프가 부드러운 모양이 되도록 X_new_7을 이용
y_pred_ridge = ridge.predict(X_new_7)

plt.plot(X, y, 'ro')
plt.plot(X_new, y_pred_ridge)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()


plt.figure(figsize=(13,7))

plt.plot(X, y, 'ro')
plt.plot(X_new, y_7_new)
plt.plot(X_new, y_pred_ridge)

plt.legend(['Original', 'Without Ridge', 'Ridge Regression'])

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()
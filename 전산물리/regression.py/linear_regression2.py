import numpy as np
from matplotlib import pyplot as plt

print(np.pi)

# true data
N = 100

# reshape = 기존 데이터는 유지하고 차원과 형상을 바꿈
# ex) 3개의 행과 4개의 열로 구성된 배열로 재설정하고 싶으면 reshape(3,4)
# reshape(N, 1) = N개 행, 1개 열
X = np.linspace(0, 2*np.pi, N).reshape(N, 1)
print(X[:5])

# plot 그리기
y = np.sin(X)
plt.plot(X,y)
plt.scatter(X,y)
plt.show()

# 랜덤 노이즈 만들어주기
np.random.seed(1)
y += 0.3*np.random.rand(N, 1)

plt.scatter(X, y)
plt.title('sine wave noise data')
plt.show()

# 기존 그래프와 함께 plotting
y = np.sin(X)
plt.plot(X, y)

# add noise
np.random.seed(1)
y += 0.3*np.random.rand(N, 1)

plt.scatter(X, y)
plt.title('sine wave data')
plt.show()

# suffle data
np.random.seed(5)

# Ndms 100이므로 0~99까지의 수를 섞어준다
idx = np.random.permutation(N)
print(idx)

shuffle_X = X[idx]
shuffle_y = y[idx]

print(shuffle_X[:3])
print(shuffle_y[:3])

# 3:1 비율로 train test를 나눔
n = int(N*(3/4))

# train data
X_train = shuffle_X[:n]
y_train = shuffle_y[:n]

# test data
X_test = shuffle_X[n:]
y_test = shuffle_y[n:]

# plot
plt.scatter(X_train, y_train, label='train')
plt.legend()
plt.title('sine wave train data')
plt.show()

plt.scatter(X_test, y_test, label='test')
plt.legend()
plt.title('sine wave test data')
plt.show()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train, y_train)

print('w0: ', reg.intercept_)
print('w1: ', reg.coef_)

Pred = reg.predict(X_train)

plt.figure()
plt.scatter(X_train, Pred, label='pred')
plt.scatter(X_train, y_train, label='target')
plt.legend()
plt.title('train data')
plt.show()

plt.figure()
plt.scatter(X_test, reg.predict(X_test), label='pred')
plt.scatter(X_test, y_test, label='target')
plt.legend()
plt.title('test data')
plt.show()

# 같은 모델로 테스트 한게 아니라 test 세트에 맞춘 또 다른 모델을 찾았기 때문에 둘이 같은 직선인지 알기 위해서 weigth를 비교해볼 필요가 있다
reg = LinearRegression()
reg.fit(X_test, y_test)

print('w0: ', reg.intercept_)
print('w1: ', reg.coef_)
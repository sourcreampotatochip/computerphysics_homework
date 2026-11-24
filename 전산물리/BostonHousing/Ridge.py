import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge

# 0) Boston 데이터 불러오기 (OpenML)
#       -target 컬럼명은 'MEDV': 집값
boston = fetch_openml(name="boston", version=1, as_frame=True)
X_df = boston.data
y_data = boston.target.to_numpy(dtype=float) # (n_samples,)

print(X_df)
print("원 특성 수:", X_df.shape[1], "행:", X_df.shape[0]) # 13개의 feature

# 1) Extended features (mglearn의 load_extended_boston 과 동일 컨셉)
poly = PolynomialFeatures(degree=2, include_bias=False) # 제곱 + 모든 상호작용 = 104개의 w가 나옴
X_data = poly.fit_transform(X_df.values)
feature_names = poly.get_feature_names_out(X_df.columns)

print("X data 의 shape:", X_data.shape)
print("y data 의 shape:", y_data.shape)
print(pd.DataFrame(X_data, columns=feature_names).head())

# 2) 셔플 및 3:1 분할
N = X_data.shape[0]
np.random.seed(3)
idx = np.random.permutation(N)
print("셔플 인덱스 길이:", len(idx))

shuffle_X = X_data[idx]
shuffle_y = y_data[idx]

n = int(N * (3/4))
X_train = shuffle_X[:n]
y_train = shuffle_y[:n]
X_test = shuffle_X[n:]
y_test = shuffle_y[n:]

print("X_train:", X_train.shape, "X_test:", X_test.shape, "합:", X_train.shape[0] + X_test.shape[0])

# 2-1) 수동 표준화(훈련 통계로만)
X_mean = X_train.mean(axis=0)
X_std = X_train.std(axis=0)
X_std[X_std == 0] = 1.0 # 분산 0 보호 : "표준편차가 0 인 데이터는 표준편차 값을 1로 해라"라는 뜻

X_train_s = (X_train - X_mean) / X_std
X_test_s = (X_test - X_mean) / X_std

# X_train_s : training 데이터 값들의 평균을 0, 표준 편차를 1로 만드는 작업
# 뒤에 각 feature에 대한 w 값들을 서로 비교할 수 있도록 하기 위함


# 3) OLS(Linear Regerssion) 학습/평가- 비표준화 공간
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

def MSE(real, predict):
    return ((real - predict)**2).mean()

def get_top_bottom(data, count):
    idx_sorted = np.argsort(data)
    top_idx = idx_sorted[-count:]
    bottom_idx = idx_sorted[:count]
    top_vals = [data[i]for i in top_idx]
    bottom_vals = [data[i] for i in bottom_idx]
    return top_vals, bottom_vals

print("\n=== OLS (LinearRegression) ===")
print("Training R^2 score:{:0.2f}".format(reg.score(X_train, y_train)))
print("Test R^2 score:{:0.2f}".format(reg.score(X_test, y_test)))
print('Mean squared error:{:0.2f}'.format(MSE(y_test, y_pred)))

W = reg.coef_
top_3_idx = np.argsort(W)[-3:]
bottom_3_idx = np.argsort(W)[:3]
print("OLS 가장 높은 W 3개 =>", ["{:0.2f}".format(W[i]) for i in top_3_idx])
print("OLS 가장 낮은 W 3개 =>", ["{:0.2f}".format(W[i]) for i in bottom_3_idx])

# 4) Ridge (lambda-->alpha = 0.1, 0.5, 1, 10) - 수동 표준화 사용
ridge00 = Ridge(alpha=0.0).fit(X_train_s, y_train)
ridge005 = Ridge(alpha=0.05).fit(X_train_s, y_train)
ridge01 = Ridge(alpha=0.1).fit(X_train_s, y_train)
ridge05 = Ridge(alpha=0.5).fit(X_train_s, y_train)
ridge1 = Ridge(alpha=1.0).fit(X_train_s, y_train)
ridge10 = Ridge(alpha=10.0).fit(X_train_s, y_train)

def report_ridge(name, model):
    pred = model.predict(X_test_s)
    print(f"[alpha={name}] Training R^2: {model.score(X_train_s, y_train):0.2f} | "
          f"Test R^2: {model.score(X_test_s, y_test):0.2f} | "
          f"MSE: {MSE(y_test, pred):0.2f}")

print("\n lambda 값에 대한 train-test R^2, MSE값")
report_ridge("0.0", ridge00)
report_ridge("0.05", ridge005)
report_ridge("0.1", ridge01)
report_ridge("0.5", ridge05)
report_ridge("1.0", ridge1)
report_ridge("10.0", ridge10)

# 5) alpha 스윕 (0.1 ~ 10.0 까지 0.1 간격)
alpha = [i / 10 for i in range(0, 101)]
train_score, test_score = [], []

for a in alpha:
    m = Ridge(alpha=a)
    m.fit(X_train_s, y_train)
    train_score.append(m.score(X_train_s, y_train))
    test_score.append(m.score(X_test_s, y_test))

plt.figure()
plt.grid(linestyle='--')
plt.plot(alpha, train_score, label="Train Score")
plt.plot(alpha, test_score, label="Test Score")
plt.title("Ridge Score (Boston, degree=2, manual standardization)")
plt.legend(loc='best')
plt.xlabel("Alpha")
plt.ylabel("R^2 Score")
plt.ylim(0, 1)
plt.show()


# 6) 계수 크기 비교 (표준화 공간 계수)
coef_ridge01 = ridge01.coef_
coef_ridge05 = ridge05.coef_
coef_ridge1 = ridge1.coef_
coef_ridge10 = ridge10.coef_

# 공정 비교용: OLS도 표준화 공간에서 다시 학습
reg_std = LinearRegression().fit(X_train_s, y_train)
W_std = reg_std.coef_

# reg_std, W_std: 모든 feature들의 값이 다르기 때문에 각 feature의 평균을 0, 표준 편차를 1로 해서 각 feature에 대한 w 값들을 서로 비교할 수 있도록 하는 작업

plt.figure(figsize=(13, 7))
plt.plot(W,         'p', label="OLS (no scaling)") # 비표준화 공간
plt.plot(W_std,     'x', label="OLS (std space)") # 표준화 공간
plt.plot(coef_ridge01, '.', label = "Ridge alpha=0.1 (std)")
plt.plot(coef_ridge05, 'v', label="Ridge alpha=0.5 (Std)")
plt.plot(coef_ridge1, 'o', label="Ridge alpha=1 (std)")
plt.plot(coef_ridge10, 'P', label="Ridge alpha=10 (std)")

# 다양한 계수들을 하나로 모아 범위 산정
stacked = np.concatenate([W, W_std, coef_ridge01, coef_ridge05, coef_ridge1, coef_ridge10])
max_abs = np.max(np.abs(stacked))
plt.ylim(-1.1 * max_abs, 1.1*max_abs)

plt.legend(loc='center', bbox_to_anchor=(1.2, 0.5))
plt.ylabel("W values")
plt.title("Coefficient Comparison (Boston degree=2, std space)")
plt.tight_layout()
plt.show()
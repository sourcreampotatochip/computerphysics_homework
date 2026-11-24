import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import pandas as pd

from sklearn.datasets import load_iris
iris_dataset = load_iris()

type(iris_dataset)

print("key value from iris_dataset:", iris_dataset.keys())

print(iris_dataset['DESCR'])
print(iris_dataset['DESCR'][:500] + "\n...")

print("feature_name value from iris_dataset:", iris_dataset['feature_names'])
print("target_names value from iris_dataset:", iris_dataset['target_names'])

iris = pd.read_csv("iris.csv")
print (iris.head())

x_iris = iris[["sepal.length","sepal.width","petal.length","petal.width"]]
y_iris = iris[["variety"]]

# 컬럼값 변경
x_iris_colums = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
x_iris.colums = x_iris_colums
print(x_iris.head(5))

print(y_iris)
print(y_iris['variety'].unique())

print("x_axis", x_iris_colums)
print("y_axis", y_iris)

# 함수를 이용해서 나누기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_iris, y_iris, test_size=0.3, random_state=0)

print("x_train 크기: {}".format(x_train.shape))
print("y_train 크기: {}".format(y_train.shape))

print("x_test 크기: {}".format(x_test.shape))
print("x_test 크기: {}".format(x_test.shape))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

print(x_train)

print(y_train)

print(y_train.shape)
print(y_train.values.ravel().shape)

## knn 알고리즘 training
knn.fit(x_train, y_train.values.ravel())

import numpy as np

# 'sepal length (cm)', 'sepal width (cm)', 'eatal length (cm)', 'petal width (cm)'을 임의로 정한다
# 5, 2.9, 1, 0.2 의 수치로 정함
Our_x = np.array([[5, 2.9, 1, 0.2]])
print(Our_x)

# 임의의 데이터로 prediction
prediction = knn.predict(Our_x)
print("예측: {}".format(prediction))

y_pred = knn.predict(x_test)
print("테스트 세트에 대한 예측값:\n {}".format(y_pred))

# y_test를 1차원 matrix로 변경
y_test_flatten = np.array(y_test).flatten()


print("테스트 세트의 정확도: {:.2f}".format(np.mean(y_pred == y_test_flatten)))

print("테스트 세트의 정확도: {:.2F}".format(knn.score(x_test, y_test_flatten)))

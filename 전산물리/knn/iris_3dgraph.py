from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

iris = datasets.load_iris()

# 1. 3D subplots 생성 (projection="3d" 설정)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# 2. 3개의 특성을 X, Y, Z 데이터로 선택
# 0: sepal length, 1: sepal width, 2: petal length
scatter = ax.scatter(
    iris.data[:, 1], 
    iris.data[:, 2], 
    iris.data[:, 3], 
    c=iris.target, 
    cmap='viridis',
    s=40 # 점 크기
)

# 3. 각 축 레이블 설정
ax.set_xlabel(iris.feature_names[1])
ax.set_ylabel(iris.feature_names[2])
ax.set_zlabel(iris.feature_names[3])

# 4. 범례 추가
ax.legend(
    scatter.legend_elements()[0],
    iris.target_names,
    loc="lower right",
    title="Classes"
)
ax.view_init(elev=30, azim=45)
plt.title("Iris Data 3D Scatter Plot")
plt.show()
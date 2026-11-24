from sklearn import datasets

# 붓꽃 데이터셋 로드
iris = datasets.load_iris()

# 데이터 전체 출력
print("Iris Dataset Overview\n")
print("Keys:", iris.keys(), "\n")

print("Description:\n", iris['DESCR'][:2000], "\n...") #설명이 길어 일부만 출력
print("\nFeature Names:\n", iris['feature_names'], "\n")
print("Target Names:\n", iris['target_names'], "\n")

print("Data (features):\n", iris['data'], "\n")
print("Target (class labels):\n", iris['target'])

import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
iris_df['target'] = iris['target']

iris_df.to_csv("iris_dataset.csv", index=False) # 현재 작업 디렉토리에 저장
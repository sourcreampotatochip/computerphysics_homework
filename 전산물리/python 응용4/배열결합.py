import numpy as np

# 1차원 배열 결합
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate([arr1, arr2])
print(result)

# 2차원 배열 결합
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
result_axis0 = np.concatenate((arr3, arr4), axis=0)
result_axis1 = np.concatenate((arr3, arr4), axis=1)
print(result_axis0)

print(result_axis1)

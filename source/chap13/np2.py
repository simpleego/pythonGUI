import numpy as np

# 1차원 배열 생성
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr1d.shape)  # 출력: (5,) - 1차원 배열이며, 5개의 원소를 가짐
print(arr2d.shape)  # 출력: (3, 3) - 3x3 행렬
print(arr2d.size)       # 출력: 9 - 원소 개수가 9개


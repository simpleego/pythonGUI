import numpy as np

# 1차원 배열 생성
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 인덱싱
print(arr1d[0])     # 출력: 1

# 슬라이싱
print(arr1d[1:4])       # 출력: [2 3 4]
print(arr2d[1, 1])  # 출력: 5
print(arr2d[:, 1])      # 출력: [2 5 8]



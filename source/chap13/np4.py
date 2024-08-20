import numpy as np
# 배열간 연산
arr = np.array([1, 2, 3])
result = arr * 2
print(result)       # 출력: [2 4 6]

# 배열의 브로드캐스팅
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = matrix + 10
print(result)

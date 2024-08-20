import numpy as np

# 두 배열 생성
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

B = np.array([10, 20, 30, 40])

# 브로드캐스팅을 이용한 배열 간 연산
result = A +B
print(result)

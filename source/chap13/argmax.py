import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# 최대값의 인덱스
max_index = np.argmax(arr)
print(max_index)        # 출력: 4 (최대값 50의 인덱스)

# 최소값의 인덱스
min_index = np.argmin(arr)
print(min_index)        # 출력: 0 (최소값 10의 인덱스)




import numpy as np
arr = np.array([3, 1, 5, 4, 2])

# 오름차순 정렬
sorted_arr = np.sort(arr)
print(sorted_arr)           # 출력: [1 2 3 4 5]

# 내림차순 정렬
reverse_sorted_arr = np.sort(arr)[::-1]
print(reverse_sorted_arr)       # 출력: [5 4 3 2 1]



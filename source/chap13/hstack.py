import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 수평으로 배열 결합
hstack_result = np.hstack((arr1, arr2))
print(hstack_result)        


# 수직으로 배열 결합
vstack_result = np.vstack((arr1, arr2))
print(vstack_result)




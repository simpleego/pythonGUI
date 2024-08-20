import numpy as np

np.random.seed(42)
random_data1 = np.random.rand(3)
print(random_data1) # 출력: [0.37454012 0.95071431 0.73199394]

np.random.seed(42)      # 시드를 동일하게 설정하면 같은 난수를 얻을 수 있음
random_data2 = np.random.rand(3)
print(random_data2) # 출력: [0.37454012 0.95071431 0.73199394]


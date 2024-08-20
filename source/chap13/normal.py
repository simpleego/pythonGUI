import numpy as np
import matplotlib.pyplot as plt

# 정규 분포를 따르는 난수 생성
mean = 0     # 평균
std = 1      # 표준편차
num_samples = 1000  # 샘플 개수

data = np.random.normal(mean, std, num_samples)

# 히스토그램으로 정규 분포 시각화
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Normal Distribution Histogram')
plt.grid(True)
plt.show()

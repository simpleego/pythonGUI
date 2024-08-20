import random
import numpy as np
import matplotlib.pyplot as plt

# 0부터 100까지의 랜덤한 정수 1000개 생성
data = np.random.randint(0, 100, 1000)

# 히스토그램 그리기
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# 그래프 제목과 축 레이블 설정
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 그래프 표시
plt.show()

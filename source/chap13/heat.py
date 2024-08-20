import random
import matplotlib.pyplot as plt
import numpy as np


# 10x10 크기의 랜덤한 2차원 데이터 생성
data = np.random.rand(10, 10)

# 히트맵 그리기
plt.imshow(data, cmap='viridis', interpolation='nearest')

# 컬러바 추가
plt.colorbar()

# 그래프 제목과 축 레이블 설정
plt.title('Heatmap of 2D Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 표시
plt.show()


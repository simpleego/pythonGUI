import random
import matplotlib.pyplot as plt
import numpy as np

# 3개의 랜덤한 정규 분포 데이터 생성
data1 = np.random.normal(5, 1, 100)  # 평균 50, 표준편차 10의 정규분포
data2 = np.random.normal(10, 2, 100)   # 평균 30, 표준편차 5의 정규분포
data3 = np.random.normal(15, 1.5, 100)  # 평균 70, 표준편차 15의 정규분포

# 이상치 추가
outliers = [30, 35, 40]

# 데이터를 하나로 합치기
data = [data1, data2, data3, outliers]

# 상자 그림 그리기
plt.boxplot(data)

# 그래프 제목과 축 레이블 설정
plt.title('Box Plot of Random Data')
plt.xlabel('Data Distribution')
plt.ylabel('Value')

# 그래프 표시
plt.show()

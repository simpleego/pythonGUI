import numpy as np
import matplotlib.pyplot as plt

height = np.random.normal(170, 5, 100)  # 평균 170, 표준편차 5의 정규분포
weight = 0.7 * height +np.random.normal(0, 5, 100)  # 키에 비례하는 몸무게 + 노이즈

plt.scatter(height, weight, label='Data', color='blue', alpha=0.6) # 산점도 그리기

coefficients = np.polyfit(height, weight, 1)  # 1차원(직선) 회귀선 계수 계산
regression_line = np.poly1d(coefficients)  # 회귀선 방정식 생성
x_values = np.linspace(min(height), max(height), 100)

plt.plot(x_values, regression_line(x_values), label='Regression Line', color='red')
plt.title('Scatter Plot with Regression Line')  # 그래프 제목과 축 레이블 설정
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

plt.legend()            # 범례 추가
plt.show()          # 그래프 표시

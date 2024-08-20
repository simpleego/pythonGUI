import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()      # 그래프의 틀(figure) 생성
ax = fig.add_subplot(111, projection='3d')  # 3D 서브플롯 생성

x = np.linspace(-5, 5, 100) # x축 데이터 생성: -5부터 5까지 100개의 값을 가진 배열
y = np.linspace(-5, 5, 100) # y축 데이터 생성: -5부터 5까지 100개의 값을 가진 배열

X, Y = np.meshgrid(x, y)    # x, y 값을 조합하여 2차원 그리드 생성

# z축 데이터 생성: sin(sqrt(x^2 + y^2))의 값을 계산하여 2차원 배열로 저장
Z = np.sin(np.sqrt(X**2 +Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')    # 3D 표면 그래프 그리기
ax.set_xlabel('X-axis') # x축 레이블 설정
ax.set_ylabel('Y-axis') # y축 레이블 설정
ax.set_zlabel('Z-axis') # z축 레이블 설정
ax.set_title('3D Surface Plot') # 그래프 제목 설정

plt.show()          # 그래프 표시

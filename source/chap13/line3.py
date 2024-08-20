import matplotlib.pyplot as plt
X = [ "Mon", "Tue", "Wed", "Thur", "Fri",  "Sat", "Sun" ] 
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]

plt.plot(X, Y)
plt.xlabel("day")           # x축 레이블
plt.ylabel("temperature")   # y축 레이블
plt.show()

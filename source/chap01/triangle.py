import turtle # turtle 모듈을 불러옵니다.

t = turtle.Turtle() # 거북이 객체를 생성합니다.
t.shape("turtle") # 거북이의 모양을 거북이로 설정합니다.

t.forward(100) # 거북이를 100 단위만큼 앞으로 이동시킵니다.
t.left(120) # 거북이를 왼쪽으로 120도 회전시킵니다.
t.forward(100) # 거북이를 다시 100 단위만큼 앞으로 이동시킵니다.
t.left(120) # 거북이를 다시 왼쪽으로 120도 회전시킵니다.
t.forward(100) # 거북이를 마지막으로 100 단위만큼 앞으로 이동시킵니다.

turtle.done() # 그림을 완성하고 창을 닫습니다.

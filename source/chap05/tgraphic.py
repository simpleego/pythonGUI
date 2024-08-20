import turtle
import random

# 초기화
turtle.speed(0)
turtle.bgcolor('black')

# 색상 리스트
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']

# 화려한 모양 그리기 함수
def draw_shape(size):
    for _ in range(6):
        turtle.color(random.choice(colors))
        turtle.forward(size)
        turtle.left(60)

# 화려한 그림 그리기 함수
def draw_art():
    for _ in range(36):
        draw_shape(100)
        turtle.right(10)

draw_art()
turtle.mainloop()

import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')
turtle.hideturtle()

# 꽃 클래스 정의
class Flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.petals = 6
        self.petal_length = 100
        self.petal_width = 25
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        self.draw_flower()
    def draw_petal(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(random.choice(self.colors))
        turtle.begin_fill()
        for _ in range(2):
            turtle.circle(self.petal_length, 60)
            turtle.left(120)
        turtle.end_fill()
    def draw_flower(self):
        for _ in range(self.petals):
            self.draw_petal()
            turtle.right(360 / self.petals)

# 꽃 그리기 함수
def draw_flowers():
    flowers = []
    for _ in range(5):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        flower = Flower(x, y)
        flowers.append(flower)

draw_flowers()
turtle.mainloop()

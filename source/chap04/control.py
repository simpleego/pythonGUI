import turtle

# 터틀 객체 생성
my_turtle = turtle.Turtle()
my_turtle.width(10)
my_turtle.shape("turtle")
my_turtle.color("brown")

# 사용자 입력을 받아 터틀 움직이기
user_input = ""

while user_input.lower() != "quit":
    user_input = input("명령어를 입력하시오: (left, right, forw, back, quit): ")
    if user_input.lower() == "left":
        my_turtle.left(90)
    elif user_input.lower() == "right":
        my_turtle.right(90)
    elif user_input.lower() == "forw":
        my_turtle.forward(100)
    elif user_input.lower() == "back":
        my_turtle.backward(100)

turtle.done()

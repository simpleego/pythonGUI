import turtle

turtle.speed(0)  # 거북이 그리기 속도 설정 (0: 가장 빠름)
turtle.bgcolor('black')  # 배경색 설정

# 각 도형의 좌표 정보를 딕셔너리로 저장합니다.
shapes = {
    'triangle': [(0, 100), (-100, -100), (100, -100)],
    'square': [(-50, 50), (-50, -50), (50, -50), (50, 50)],
    'pentagon': [(0, 100), (-95, 30), (-58, -80), (58, -80), (95, 30)],
    'hexagon': [(-60, 90), (-90, 30), (-60, -30), (60, -30), (90, 30), (60, 90)],
}

def draw_shape(shape_name):
    turtle.color('white')  # 펜 색상을 흰색으로 설정
    turtle.penup()  # 펜을 들어서 이동할 때 선을 그리지 않음
    coords = shapes[shape_name]  # 해당 도형의 좌표 정보를 가져옴
    turtle.goto(coords[0])  # 시작 지점으로 이동
    turtle.pendown()  # 펜을 내려서 선을 그리기 시작
    for coord in coords[1:]:
        turtle.goto(coord)  # 도형의 모든 좌표를 순회하며 선을 그림
    turtle.goto(coords[0])  # 시작 지점으로 다시 돌아옴 (도형을 닫음)

def draw_all_shapes():
    for shape_name in shapes:
        draw_shape(shape_name)  # 모든 도형을 그립니다.
        turtle.penup()
        turtle.forward(150)  # 도형 사이의 간격 조절
        turtle.pendown()

draw_all_shapes()  # 모든 도형을 그리고 배치합니다.
turtle.mainloop()  # 사용자의 입력을 기다림

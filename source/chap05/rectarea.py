# 사각형의 넓이를 계산하는 함수
def area(w, h):
    return w * h

# 양수 입력을 받는 함수
def input_pos(msg):
    while True:
        value = int(input(msg))  # 사용자로부터 정수 값을 입력받습니다.
        if value > 0:
            return value  # 양수일 경우 입력을 반환하고 반복문을 종료합니다.
        else:
            print('양수만 입력하시오.')  # 양수가 아닐 경우 메시지를 출력하고 다시 입력 요구

# 사용자로부터 가로와 세로의 길이를 입력받습니다.
width = input_pos('사각형의 가로: ')
height = input_pos('사각형의 세로: ')

# 면적을 계산하고 출력합니다.
result = area(width, height)
print('면적=', result)

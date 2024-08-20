PI = 3.14159265358979   # 전역 변수, 원주율 값

def main():
    radius = float(input('원의 반지름을 입력하시오: '))  # 사용자로부터 반지름을 입력받습니다.
    print('원의 면적:', circleArea(radius))  # 원의 면적을 출력합니다.
    print('원의 둘레:', circleCircumference(radius))  # 원의 둘레를 출력합니다.

def circleArea(radius):
    return PI * radius * radius   # 원의 면적을 계산하여 반환합니다.

def circleCircumference(radius):
    return 2 * PI * radius   # 원의 둘레를 계산하여 반환합니다.

main()  # main 함수를 호출하여 프로그램을 실행합니다.

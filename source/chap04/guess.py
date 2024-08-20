import random

tries = 0  			# 시도 횟수 초기화
number = random.randint(1, 100)  # 1부터 100 사이의 랜덤 숫자 생성

print("1부터 100 사이의 숫자를 맞추시오")

while tries < 10:
    guess = int(input("숫자를 입력하시오: "))  	# 사용자로부터 숫자를 입력받음
    tries = tries + 1  				# 시도 횟수 증가
    if guess < number:
        print("낮음!")  			# 입력한 숫자가 비밀번호보다 작을 경우 출력
    elif guess > number:
        print("높음!")  			# 입력한 숫자가 비밀번호보다 클 경우 출력
    else:
        break  				# 비밀번호를 맞춘 경우 반복문 종료

if guess == number:
    print("축하합니다. 시도횟수=", tries)  # 비밀번호를 맞춘 경우 축하 메시지와 시도 횟수 출력
else:
    print("정답은 ", number)  # 시도 횟수를 모두 소진하여 맞추지 못한 경우 정답 출력

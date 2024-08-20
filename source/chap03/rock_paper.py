import random

# 사용자 입력 받기
user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")

# 컴퓨터 랜덤 선택
choices = ["가위", "바위", "보"]
computer_choice = random.choice(choices)

# 선택 출력
print("사용자 선택:", user_choice)
print("컴퓨터 선택:", computer_choice)

# 승패 결정
if user_choice == computer_choice:
    print("무승부입니다!")
elif (user_choice == "가위"and computer_choice == "보") or (user_choice == "바위"and computer_choice == "가위") or (user_choice == "보"and computer_choice == "바위"):
    print("사용자가 이겼습니다!")
else:
    print("컴퓨터가 이겼습니다!")

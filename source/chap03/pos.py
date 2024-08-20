food_cost = float(input("음식 값 입력: "))

print("팁을 선택하세요:")
print("1. 10%")
print("2. 15%")
print("3. 20%")

tip_choice = int(input("팁 선택 (1/2/3): "))
if tip_choice == 1:
    tip_percent = 0.10
elif tip_choice == 2:
    tip_percent = 0.15
elif tip_choice == 3:
    tip_percent = 0.20
else:
    print("올바른 선택이 아닙니다. 기본값인 15%로 계산합니다.")
    tip_percent = 0.15

tip_amount = food_cost * tip_percent
total_cost = food_cost + tip_amount

print(f"음식 값: ${food_cost:.2f}")
print(f"선택한 팁: {tip_percent*100}%")
print(f"팁 금액: ${tip_amount:.2f}")
print(f"총 지불 금액: ${total_cost:.2f}")

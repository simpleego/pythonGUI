def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
    return total, average, max_value, min_value

# 사용자로부터 숫자들을 입력받아 리스트에 추가합니다.
numbers = []
while True:
    num = input("숫자를 입력하세요 (종료는 'q'): ")
    if num.lower() == 'q':
        break
    numbers.append(int(num))

# 리스트에 있는 숫자들의 합계, 평균, 최대값, 최소값을 계산합니다.
total, average, max_value, min_value = calculate_stats(numbers)
print("숫자들의 합계:", total)
print("숫자들의 평균:", average)
print("숫자들의 최대값:", max_value)
print("숫자들의 최소값:", min_value)

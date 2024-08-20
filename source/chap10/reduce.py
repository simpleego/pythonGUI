from functools import reduce
numbers = [1, 2, 3, 4, 5]

# reduce 함수를 사용하여 모든 숫자를 더함
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 출력: 15

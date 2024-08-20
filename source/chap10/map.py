# 리스트의 각 요소를 제곱하여 새로운 리스트 생성
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)          	# 출력: [1, 4, 9, 16, 25]

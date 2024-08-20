# 리스트에서 짝수만 걸러내는 새로운 리스트 생성
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)         # 출력: [2, 4, 6, 8]

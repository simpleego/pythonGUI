squares = [0, 1, 4, 9, 16, 25, 36, 49]
print(squares[3:6])  	# 슬라이싱은 새로운 리스트를 반환한다. 

my_list = [1, 2, 3, 4, 5]
print(my_list[:3])
print(my_list[2:])
print(my_list[:])

squares = [0, 1, 4, 9, 16, 25, 36, 48]	# 잘못된 부분이 있음!
squares[7] = 49  				# 잘못된 값을 변경할 수 있음!
print(squares)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']	# 리스트의 일부를 변경해보자.
print(letters)

letters[2:5] = []			# 리스트의 일부를 삭제해보자. 
print(letters)

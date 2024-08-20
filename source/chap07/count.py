text = "apple orange apple banana apple"

count_apple = text.count("apple")
print(count_apple)  		# 출력: 3

count_fruit = text.count("fruit")
print(count_fruit)  		# 출력: 0

count_a = text.count("a", 4, 15)
print(count_a)  			# 출력: 2

numbers = { 2, 1, 3 }
# print(numbers[0])

numbers.add(4)
print(numbers)
numbers.update([2, 3, 4, 5])
print(numbers)

numbers.discard(5)
print(numbers)

# numbers.move(6)	# 예외가 발생된다. 

numbers.clear()	# 세트의 크기가 0이 된다. 

numbers = [9, 5, 2, 1, 7]
numbers.sort()  			# 오름차순으로 정렬
print(numbers)  			

numbers.sort(reverse=True)  		# 내림차순으로 정렬
print(numbers) 			 

names = ['Alice', 'Bob', 'Charlie', 'David']
names.sort() 			 # 알파벳순으로 정렬
print(names)  			

people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 19}, {'name': 'Charlie', 'age': 21}]
people.sort(key=lambda x: x['age'])  # 나이를 기준으로 정렬
print(people)

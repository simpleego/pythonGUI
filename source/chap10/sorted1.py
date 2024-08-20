numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)  # 오름차순으로 정렬
print(sorted_numbers)  		
 
names = ['Kim', 'Lee', 'Park', 'Choi']
sorted_names = sorted(names)  	# 알파벳순으로 정렬
print(sorted_names)  		

sorted_names_reverse = sorted(names, reverse=True)  # 알파벳역순으로 정렬
print(sorted_names_reverse)  	


names = ['Kim', 'Lee', 'Park', 'Choi']
sorted_names_length = sorted(names, key=len)  	# 길이를 기준으로 정렬
print(sorted_names_length)  	


people = [
	{'name': 'Kim', 'age': 25}, 
	{'name': 'Lee', 'age': 19}, 
	{'name': 'Park', 'age': 21}
]

sorted_people = sorted(people, key=lambda x: x['age'])  # 나이를 기준으로 정렬
print(sorted_people)

sorted_people_reverse = sorted(people, key=lambda x: x['age'], reverse=True)

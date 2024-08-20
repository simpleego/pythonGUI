print(abs(-3))
print(abs(3+4j))
print(divmod(10, 3))
x = complex(4, 2)
print(x)

list1 = [True, True, True, True]
result1 = all(list1)		# 리스트의 모든 요소가 참인 경우
print(result1)  

string1 = "Hello"
result4 = all(char.isalpha() for char in string1)	 # 문자열의 모든 문자가 참인 경우
print(result4)  

list1 = [False, True, False, False]
result1 = any(list1)		# 리스트의 요소 중 하나라도 참인 경우
print(result1)  

string1 = "Hello, World!"
result4 = any(char.isdigit() for char in string1)	# 문자열의 요소 중 하나라도 참인 경우
print(result4)  

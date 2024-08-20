statement = input("문자열을 입력하시오: ")  # 사용자로부터 문자열을 입력받음
alphas = 0   		# 알파벳 문자 개수를 저장하는 변수 초기화
digits = 0   		# 숫자 문자 개수를 저장하는 변수 초기화
spaces = 0   		# 공백 문자 개수를 저장하는 변수 초기화

# 입력된 문자열을 순회하면서 각각의 문자가 알파벳인지, 숫자인지, 혹은 공백인지 판별
for c in statement:
   if c.isalpha():   		# c가 알파벳인지 판별
      alphas = alphas + 1   	# 알파벳 문자의 개수 증가
   if c.isdigit():   		# c가 숫자인지 판별
      digits = digits + 1   		# 숫자 문자의 개수 증가
   if c.isspace():   		# c가 공백인지 판별
      spaces = spaces + 1   	# 공백 문자의 개수 증가

# 각 문자 종류별 개수를 출력
print("알파벳 문자의 개수=", alphas)
print("숫자 문자의 개수=", digits)
print("스페이스 문자의 개수=", spaces)

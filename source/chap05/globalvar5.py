count = 0

def increment_global():
    global count  	# 전역 변수 count를 사용하겠다고 명시
    count += 1

def print_count():
    print("현재 count 값:", count)

increment_global()
increment_global()
print_count()  		# 출력: 현재 count 값: 2

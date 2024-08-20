keyword_list = []  	# 사용자로부터 입력받은 단어를 저장할 빈 리스트 생성
user_input = ""  		# 사용자 입력을 저장할 변수 초기화

# 'quit'이 입력되기 전까지 사용자로부터 단어를 입력받음
while user_input != "quit":
    user_input = input("단어를 입력하세요 ('quit'으로 종료): ")
    if user_input != "quit":  	# 사용자 입력이 'quit'이 아니면 리스트에 추가
        keyword_list.append(user_input)

keyword_count = len(keyword_list) 		# 입력된 단어 개수를 계산
print("입력된 단어 개수:", keyword_count)  	# 입력된 단어 개수 출력
print("입력된 단어 목록:", keyword_list)  	# 입력된 단어 목록 출력

# 빈 영어-한국어 사전을 생성합니다.
english_dict = dict()

# 영어 단어와 그에 해당하는 한국어 단어를 사전에 추가합니다.
english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

# 사용자로부터 단어를 입력받습니다.
word = input("단어를 입력하시오: ")

# 입력한 단어가 사전에 있으면 해당 한국어 단어를 출력하고,
# 없으면 "없음"을 출력합니다.
print(english_dict.get(word, "없음"))

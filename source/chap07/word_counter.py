input_string = input("문자열을 입력하시오: ")

# 입력 문자열을 공백을 기준으로 단어로 분리합니다.
words = input_string.split()

# 단어 등장 횟수를 저장할 딕셔너리를 초기화합니다.
word_count = {}

# 각 단어의 등장 횟수를 계산합니다.
for word in words:
    word = word.lower()	    # 단어를 소문자로 변환하여 등장 횟수를 세어줍니다.
    
    # 딕셔너리에 단어가 이미 있는지 확인하고, 없으면 1로 초기화합니다.
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1	        # 이미 있는 단어인 경우 등장 횟수를 1 증가시킵니다.

for word, count in word_count.items():
    print(f"'{word}': {count}번")

def count_unique_words(text):
    # 입력받은 문자열을 공백을 기준으로 단어로 분리
    words = text.split()
    
    # 중복을 제거하기 위해 단어들을 집합(set)에 추가
    unique_words = set(words)
    
    # 중복을 제거한 단어의 개수 반환
    return len(unique_words)

# 사용자로부터 문자열 입력 받기
user_input = input("문자열을 입력하세요: ")

# 중복되지 않은 단어의 개수 계산
result = count_unique_words(user_input)
print("중복되지 않은 단어의 개수:", result)

original = input('문자열을 입력하시오: ')     # 사용자로부터 문자열을 입력 받습니다.
word = original.lower()             # 입력 받은 문자열을 소문자로 변환합니다.

if len(original) > 0 and original.isalpha():    # 입력된 문자열이 알파벳 문자이면 
    for index, char in enumerate(word):      # 문자와 인덱스를 함께 가져온다. 
        if char in 'aeiou':             # 현재 문자가 모음인지 확인합니다.
            print(f"모음 '{char}'이(가) {index}번째 위치에 있습니다.")  

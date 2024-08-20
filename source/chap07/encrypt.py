def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # 알파벳 문자인 경우만 암호화 진행
            char_code = ord(char)
            if char.islower():
                # 소문자 알파벳의 경우
                encrypted_code = ((char_code - ord('a') + shift) % 26) + ord('a')
            else:
                # 대문자 알파벳의 경우
                encrypted_code = ((char_code - ord('A') + shift) % 26) + ord('A')
            encrypted_char = chr(encrypted_code)
            encrypted_text += encrypted_char
        else:
            # 알파벳이 아닌 문자는 그대로 유지
            encrypted_text += char
    return encrypted_text

# 사용자로부터 입력 받기
input_text = input("암호화할 문자열을 입력하세요: ")
shift_amount = int(input("암호화에 사용할 시프트 값을 입력하세요 (양수 또는 음수): "))
# 문자열 암호화
encrypted_text = encrypt(input_text, shift_amount)
print("암호화된 문자열:", encrypted_text)

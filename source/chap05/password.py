
import random  # random 모듈을 가져옵니다.

def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"  # 사용할 문자열을 정의합니다.
    password = ""  # 비밀번호를 저장할 변수를 초기화합니다.

    # 6번 반복하면서 무작위 문자를 비밀번호에 추가합니다.
    for i in range(6):
        index = random.randrange(len(alphabet))  # 무작위로 문자열의 인덱스를 선택합니다.
        password = password + alphabet[index]  # 선택한 문자를 비밀번호에 추가합니다.
    
    return password  # 생성한 비밀번호를 반환합니다.

# genPass 함수를 호출하여 무작위 비밀번호를 생성하고 출력합니다.
print(genPass())
print(genPass())
print(genPass())

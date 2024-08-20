dogNames = []  # 빈 리스트를 생성합니다.

while True:  # 무한 루프를 시작합니다.
    name = input('강아지의 이름을 입력히시오(종료시에는 엔터키): ')  # 사용자로부터 입력을 받습니다.
    if name == '':  # 만약 입력이 없다면(엔터키를 누르면),
        break  # 무한 루프를 종료합니다.
    dogNames.append(name)  # 입력 받은 이름을 리스트에 추가합니다.

print('강아지들의 이름:')  # 리스트에 저장된 강아지들의 이름을 출력합니다.
for name in dogNames:
    print(name, end=", ")  # 각 이름을 출력하고 콤마(,)로 구분하여 출력합니다.

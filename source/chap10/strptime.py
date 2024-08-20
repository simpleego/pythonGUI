from datetime import datetime

# 사용자로부터 날짜 문자열 입력 받기
date_string = input("날짜를 입력하세요 (예: 2023-12-10): ")

try:
    # strptime() 함수를 사용하여 문자열을 날짜 객체로 변환
    date_object = datetime.strptime(date_string, "%Y-%m-%d")

    # 변환된 날짜 객체 출력
    print("입력한 날짜 객체:", date_object)

except ValueError:
    print("잘못된 형식의 날짜입니다. 올바른 형식으로 다시 입력하세요.")

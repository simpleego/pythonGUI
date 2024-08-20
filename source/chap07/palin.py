string = input("문자열을 입력하시오: ")

# 문자열을 뒤집어서 비교하여 회문인지 검사
reversed_string = string[::-1]

if string == reversed_string:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

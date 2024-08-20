add = lambda x, y : x + y

result = add(3, 5)
print(result) # 출력 결과: 8

def add2(x, y) :
    return x+y
result = add2(3, 5)
print(result) # 출력 결과: 8


# 문자열의 길이를 반환하는 람다 함수
string_length = lambda s : len(s)
# 두 수 중에서 더 큰 값을 반환하는 람다 함수
max_number = lambda x, y : x if x > y else y

def simple_generator():
    yield 1
    yield 2
    yield 3

# 제너레이터 객체 생성
gen = simple_generator()

# for 루프를 사용하여 제너레이터의 값들을 순회
for value in gen:
    print(value, end=" ")

class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 현재 값이 최대값 미만이면 다음 값을 반환하고, 현재 값을 증가시킵니다.
        if self.current < self.max_value:
            result = self.current
            self.current += 1
            return result
        # 최대값 이상이면 StopIteration 예외를 발생시킵니다.
        else:
            raise StopIteration
# 이터레이터 객체 생성
my_iterator = MyIterator(5)

# for 루프를 사용하여 이터레이터의 요소들을 순회
for value in my_iterator:
    print(value)

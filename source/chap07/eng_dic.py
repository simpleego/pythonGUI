def print_values(a, b, c) :
        print(a, b, c)
my_list = [1, 2, 3]
print_values(*my_list) # 리스트의 요소들을 각각의 인자로 풀어서 함수에 전달

# 출력: 1 2 3
def print_info(name, age) :
        print(f"Name: {name}, Age: {age}")
my_dict = {'name': 'Alice', 'age': 30}
print_info(**my_dict) # 딕셔너리의 키와 값들을 인자로 풀어서 함수에 전달

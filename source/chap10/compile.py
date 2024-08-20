# 컴파일할 파이썬 코드 문자열
python_code = '''
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10)
print("Result:", result)
'''

# 코드 컴파일하기
compiled_code = compile(python_code, '<string>', 'exec')

# 컴파일된 코드 실행하기
exec(compiled_code)

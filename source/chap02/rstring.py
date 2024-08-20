print('C:\some\name') # 여기서 \n은 줄바꿈을 의미한다.
print(r'C:\some\name') # 문자열 앞에 r을 붙이면 \를 이스케이프 문자로 해석하지 않는다.

# 일반 문자열에서 백슬래시를 이스케이프 문자로 사용한 경우
normal_string = "C:\\Users\\Username\\Documents\\file.txt"
print(normal_string) # 출력: C:\Users\Username\Documents\file.txt
# r-문자열을 사용한 경우
raw_string = r"C:\Users\Username\Documents\file.txt"
print(raw_string) # 출력: C:\Users\Username\Documents\file.txt

names = ['Kim', 'Lee', 'Choi']
scores = [85, 92, 78]
grades = ['B', 'A', 'C']

# zip() 함수를 사용하여 시퀀스들을 묶기
zipped = zip(names, scores, grades)

# 결과를 확인하기 위해 리스트로 변환
zipped_list = list(zipped)
print(zipped_list)

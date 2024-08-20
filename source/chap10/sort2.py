students = [
    {'name': 'Kim', 'age': 21, 'grade': 'A'},
    {'name': 'Lee', 'age': 19, 'grade': 'B'},
    {'name': 'Choi', 'age': 20, 'grade': 'C'},
    {'name': 'Park', 'age': 22, 'grade': 'A'},
    {'name': 'Song', 'age': 21, 'grade': 'B'}
]

# 학생을 나이 오름차순으로 정렬하되, 나이가 같다면 성적의 역순으로 정렬
sorted_students = sorted(students, key=lambda x: (x['age'], -ord(x['grade'])))
print(sorted_students)

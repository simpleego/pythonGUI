scores = []
print("학생 3명의 성적을 입력하세요: ")

score = int(input("1번 학생의 성적을 입력하세요: "))
scores.append(score)

score = int(input("2번 학생의 성적을 입력하세요: "))
scores.append(score)

score = int(input("3번 학생의 성적을 입력하세요: "))
scores.append(score)

max_score = max(scores)
min_score = min(scores)

print(f"최고 성적: {max_score}")
print(f"최저 성적: {min_score}")

# 학생 수를 정의합니다.
STUDENTS = 5

scores = []		# 성적을 저장할 빈 리스트와 성적 합계를 초기화합니다.
scoreSum = 0

# 학생 수만큼 반복하여 성적을 입력받고 리스트에 추가하며 합계를 계산합니다.
for i in range(STUDENTS):
    value = int(input("성적을 입력하시요: "))
    scores.append(value)
    scoreSum += value

scoreAvg = scoreSum / len(scores)		# 성적의 평균을 계산합니다.

highScoreStudents = 0	# 80점 이상 성적을 받은 학생 수를 세기 위한 변수를 초기화합니다.

# 각 학생의 성적을 확인하고 80점 이상인 경우 highScoreStudents 변수를 증가시킵니다.
for i in range(len(scores)):
    if scores[i] >= 80:
        highScoreStudents += 1
print("성적 평균은", scoreAvg, "입니다.")
print("80점 이상 성적을 받은 학생은", highScoreStudents, "명입니다.")

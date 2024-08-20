import random

def quiz_game():
    questions = {
        "프랑스의 수도는?": "파리",
        "Red Planet로 알려진 행성은?": "화성",
        "2 + 2의 결과는?": "4",
        "상대성 이론을 발견한 과학자는?": "아인슈타인",
        "지구상에서 가장 큰 동물은?": "휜수염 고래"
    }

    # 문제를 무작위로 선택하여 출제
    question = random.choice(list(questions.keys()))
    correct_answer = questions[question]

    print("다음 문제에 대한 답을 입력하세요:")
    print(question)

    # 사용자 입력을 받고 정답 확인
    user_answer = input("답: ")

    if user_answer.lower() == correct_answer.lower():
        print("정답입니다!")
    else:
        print(f"오답입니다. 정답은 '{correct_answer}'입니다.")

# 퀴즈 게임 실행
quiz_game()

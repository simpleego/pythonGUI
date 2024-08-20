import random

def roll_dice():
    return random.randrange(1, 7)

# 주사위를 10번 굴려서 결과 출력
for _ in range(10):
    print(roll_dice())

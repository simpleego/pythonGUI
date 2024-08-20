from random import randint

count  = int(input('주사위 실험 반복횟수: '))
sum_count = [0,0,0,0,0,0,0,0,0,0,0]     # 2에서 12까지만

for i in range(count):
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    sum_count[die1+die2-2] += 1     # 합의 빈도수를 해당 인덱스에 증가

for i in range(2, 13):
    probability = 100*sum_count[i - 2] / count
    print(f"주사위 합 {i}의 확률: {probability}%")

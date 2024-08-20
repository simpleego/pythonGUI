year = 0       # 초기 연도를 0으로 설정
balance = 1000  # 시작 잔액을 1000으로 설정

# 잔액이 2000보다 작을 때까지 반복
while balance < 2000:   
    year = year + 1   # 연도를 1 증가시킴
    interest = balance * 0.05   # 현재 잔액에 대한 이자를 계산 (이자율은 5%로 가정)
    balance = balance + interest  # 이자를 잔액에 더함

# 반복이 끝나면 기간(year)과 최종 총액(balance) 출력
print("기간: ", year)
print("총액: ", balance)

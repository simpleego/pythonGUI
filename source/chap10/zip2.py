prices = [100, 200, 300, 400]
quantities = [2, 3, 5, 1]

# 두 리스트를 zip() 함수로 묶어서 각 요소별 곱셈 계산
total_prices = [price * quantity for price, quantity in zip(prices, quantities)]

# 결과 출력
print("물건의 총가격 = ", sum(total_prices))  

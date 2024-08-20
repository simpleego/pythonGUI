from datetime import datetime

def check_exchange_eligibility(purchase_date_str):
    try:					# 예외가 발생할 가능성이 잇는 코드
        purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        current_date = datetime.now()	        # 현재 날짜를 가져옴
        delta = current_date - purchase_date        # 날짜 간의 차이 계산

        if delta.days >= 30:
            print("30일이 넘었으므로 교환이 불가능합니다.")
        else:
            print("30일 미만이므로 교환이 가능합니다.")

    except ValueError:			# 여기서 예외를 처리한다. 
        print("올바른 날짜 형식이 아닙니다. YYYY-MM-DD 형식으로 입력해주세요.")

purchase_date_input = input("물건을 구매한 날짜를 YYYY-MM-DD 형식으로 입력하세요: ")
check_exchange_eligibility(purchase_date_input)	

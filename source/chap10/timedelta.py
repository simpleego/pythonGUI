from datetime import datetime, timedelta

# 현재 시간 가져오기
current_time = datetime.now()
print("현재 시간:", current_time)

# timedelta를 사용하여 1시간 30분 후의 시간 계산
time_interval = timedelta(hours=1, minutes=30)
future_time = current_time + time_interval

print("1시간 30분 후의 시간:", future_time)

from datetime import datetime, date, time

# 현재 날짜와 시간 가져오기
current_datetime = datetime.now()
print("현재 날짜와 시간:", current_datetime)

# 날짜와 시간 정보 분리
current_date = current_datetime.date()
current_time = current_datetime.time()

print("현재 날짜:", current_date)
print("현재 시간:", current_time)

# 날짜와 시간을 문자열로 변환
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("형식화된 날짜와 시간:", formatted_datetime)

# 문자열을 datetime 객체로 변환
date_string = "2023-07-19 14:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("파싱된 datetime 객체:", parsed_datetime)

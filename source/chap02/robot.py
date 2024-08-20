# 사용자로부터 도시명을 입력받아 변수 city에 저장한다.
city = input("도시명을 입력하세요: ")

# 사용자로부터 기온을 입력받아 실수로 변환한 뒤 변수 temperature에 저장한다.
temperature = float(input("기온을 입력하세요(예: 20.5) : "))

# 사용자로부터 날씨 상태를 입력받아 변수 weather_condition에 저장한다.
weather_condition = input("날씨 상태를 입력하세요: ")

# 입력된 정보를 사용하여 날씨 관련 뉴스 문자열을 생성한다.
news = f"\n오늘 {city}의 날씨는 {weather_condition}이며, 기온은 {temperature}도입니다. "

# 뉴스 문자열에 추가적인 문장을 덧붙인다.
news += "적당한 날씨입니다. 즐거운 하루 되세요!"

# 생성된 뉴스 문자열을 화면에 출력한다.
print(news)

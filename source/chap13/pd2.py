import pandas as pd

# 데이터 프레임 생성
data = pd.DataFrame({
'Name': ['Kim', 'Lee', 'Park'],
'Age': [25, 30, 22],
'Gender': ['Female', 'Male', 'Female']
})
# 데이터 프레임을 CSV 파일로 저장
data.to_csv('data.csv', index=False)
# 데이터 프레임을 엑셀 파일로 저장
data.to_excel('data.xlsx', index=False)

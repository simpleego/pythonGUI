import pandas as pd

# DataFrame 생성
data = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park'],
    'Age': [25, 30, 22],
    'Gender': ['Female', 'Male', 'Female']
})

# 'Age' 열을 기준으로 오름차순 정렬
data_sorted = data.sort_values(by='Age')
print(data_sorted)

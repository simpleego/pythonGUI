import pandas as pd

# DataFrame 생성
data = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park'],
    'Age': [25, 30, 22],
    'Gender': ['Female', 'Male', 'Female']
})

# 'Age' 열이 25 이상인 데이터만 선택
filtered_data = data[data['Age'] >=25]
print(filtered_data)

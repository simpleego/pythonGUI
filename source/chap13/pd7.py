import pandas as pd

# 첫 번째 DataFrame 생성
data1 = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park'],
    'Age': [25, 30, 22]
})

# 두 번째 DataFrame 생성
data2 = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'David'],
    'Gender': ['Female', 'Male', 'Male']
})

# 'Name' 열을 기준으로 두 DataFrame을 병합
merged_data = pd.merge(data1, data2, on='Name', how='inner')
print(merged_data)

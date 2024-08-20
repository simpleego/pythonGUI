import pandas as pd

# DataFrame 생성
data = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park'],
    'Age': [25, 30, 22],
    'Gender': ['Female', 'Male', 'Female']
})

# 'Gender' 열을 기준으로 그룹화하고, 각 그룹의 평균 나이 계산
grouped_data = data.groupby('Gender')['Age'].mean()
print(grouped_data)

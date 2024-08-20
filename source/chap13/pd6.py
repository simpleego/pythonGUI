import pandas as pd

# DataFrame 생성
data = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park'],
    'Age': [25, 30, 22],
    'Gender': ['Female', 'Male', 'Female']
})

# 'Age' 열의 값을 제곱하여 새로운 열 추가
data['Age_Squared'] = data['Age'].apply(lambda x: x**2)
print(data)

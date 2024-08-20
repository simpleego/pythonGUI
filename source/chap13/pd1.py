import pandas as pd

data = pd.read_excel('data.xlsx')       # Excel 파일 불러오기 (첫 번째 시트)
data = pd.read_excel('data.xlsx', sheet_name='Sheet1')  # Excel 파일 불러오기 (첫 번째 시트)

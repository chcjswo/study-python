import pandas as pd
# xlrd, openpyxl

# df = pd.read_excel('C:\\Users\\User\\workspace\\study-python\\section4\\excel_s1.xlsx', sheet_name=0)
# print(df)
# print(df.head())

# 행, 푸터 스킵
# df = pd.read_excel('C:\\Users\\User\\workspace\\study-python\\section4\\excel_s1.xlsx', sheet_name=0, skiprows=[0], skip_footer=10)
# print(df)

# 헤더정의
# df = pd.read_excel('C:\\Users\\User\\workspace\\study-python\\section4\\excel_s1.xlsx', header=0)
# print(df)
# print(list(df))

# 특정값 치환
# df = pd.read_excel('C:\\Users\\User\\workspace\\study-python\\section4\\excel_s1.xlsx', header=0, na_values='...', converters={'2003': lambda e: e if e > 60000 else None})
# print(df)


df = pd.read_excel('C:\\Users\\User\\workspace\\study-python\\section4\\excel_s2.xlsx')
# print(df)
print(df.describe().round(2))

from pandas import Series, DataFrame
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r_data = {
    'city': ['서울', '대구', '부산', '대전'],
    'total1': [55000, 43000, 88800, 23000],
    'total3': [343, 2343, 3333, 1111]
}
i_data = ['one', 'two', 'three', 'four']

# print(r_data)
# print(i_data)

# DataFrame 정의
d_frame = DataFrame(r_data, index=i_data)
# print(type(d_frame))
# print(d_frame)
# print(d_frame.index)
# print(d_frame.values)
# print(d_frame['city']) # columns
# print(d_frame.ix['one']) # rows

# 값 순회
for e in d_frame.values:
    for i, z in enumerate(e):
        print(i, z)

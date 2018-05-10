from pandas import Series

series1 = Series([92500, 23432, 34544, 234234])
print(series1)

print('count', series1.count())
print('describe', series1.describe())

# 인덱스 접근
print(series1[3])


series2 = Series([92500, 23432, 34544, 234234, 342343, 2323432], index=['11', '22', '33', '44', '55', '66'])
print(series2)

# 인덱스 순회
for idx in series2.index:
    print('index', idx)

# 값 순회
for val in series2.values:
    print('value', val)


series_g1 = Series([10, 20, 30], index=['n1', 'n2', 'n3'])
series_g2 = Series([510, 160, 270], index=['n3', 'n2', 'n1'])
print(series_g1)
print(series_g2)

sum = series_g1 + series_g2
print('sum')
print(sum)

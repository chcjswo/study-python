import matplotlib.pyplot as plt

# fig 객체 생성
fig = plt.figure()

# 서브 슬롯 생성 (2행 1열)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# x축 생성
x = list(range(0, 100))

# y축 생성
y = [v * v for v in x]

# z축 생성
z = [v * v * 2 for v in x]

# 라인 차트 (1행 1열)
ax1.plot(x, y, 'b', label='test1')

# bar 차트(2행 1열)
ax2.bar(x, z, label='test2')

plt.legend(loc='upper left')
plt.title('test chart')

plt.show()

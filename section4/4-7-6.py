import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

# 조회 시작날짜
start = datetime.datetime(2018, 2, 1)
end = datetime.datetime(2018, 2, 15)

f = web.DataReader('F', 'morningstar', start, end)
d = web.DataReader('D', 'morningstar', start, end)

print(f)
print(d)

fig = plt.figure('char~~')

fig.set_size_inches(10, 6, forward=True)

print(f['Close'])
plt.plot(f['Close'], f['High'], 'b', label='FFFF')
plt.plot(d['Close'], d['High'], 'r', label='DDDD')

plt.legend(loc='upper left')
plt.title('alsfjasld')
plt.xlabel('Close')
plt.ylabel('High')

plt.show()

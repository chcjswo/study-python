import pandas_datareader.data as web
import datetime

# 조회 시작날짜
start = datetime.datetime(2018, 2, 1)
end = datetime.datetime(2018, 2, 15)

# google 정보 호출
GS = web.DataReader('KRX: 035720', 'google', start, end)
print(GS)

# 구글 서비스 종료로 인해 실행 불가

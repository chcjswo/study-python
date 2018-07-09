import pandas_datareader.data as web
import pandas as pd
import datetime
import pymysql

# MySQLdb  생성
pymysql.install_as_MySQLdb()
import MySQLdb
from sqlalchemy import create_engine

try:
    # 엔진 생성
    engine = create_engine('mysql+mysqldb://python:' + '1111!' + '@localhost/python', encoding='utf-8')
    with engine.connect() as conn:
        # 조회 시작, 마감 날짜
        start = datetime.datetime(2018, 3, 1)
        end = datetime.datetime(2018, 5, 1)

        f = web.DataReader('F', 'morningstar', start, end)
        # f['Date'] = f.index
        f['Date'] = start
        f.index = range(1, len(f.index) + 1)
        # print(f)
        # print(f['Open'])
        # pandas to database(to_sql)
        f.to_sql('pd_datareader', conn, if_exists='replace', index=True, index_label='id') # fail, replace, append
        # conn.commit()

        df = pd.read_sql(('select * from pd_datareader'), conn, index_col = 'id')
        print(df)
finally:
    # 엔진 종료
    engine.dispose()
    print('Dataframe sql work complete!!!!')

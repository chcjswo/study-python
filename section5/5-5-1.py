import pandas_datareader.data as web
import pandas as pd
import datetime
import sqlite3

try:
    with sqlite3.connect('C:\\Users\\User\\workspace\\study-python\\section5\\database\\sqlite2.db') as conn:
        # 조회 시작, 마감 날짜
        start = datetime.datetime(2018, 3, 1)
        end = datetime.datetime(2018, 4, 1)

        f = web.DataReader('F', 'morningstar', start, end)
        f['Date'] = f.index
        f.index = range(1, len(f.index) + 1)
        # print(f)
        # print(f['Open'])
        # pandas to database(to_sql)
        # f.to_sql('pd_datareader', conn, if_exists='replace', index=True, index_label='id') # fail, replace, append
        # conn.commit()

        df = pd.read_sql(('select * from pd_datareader'), conn, index_col = 'id')
        print(df)
finally:
    print('Dataframe sql work complete!!!!')

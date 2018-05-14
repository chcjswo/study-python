import pymysql
import simplejson as json
import datetime

# mysql connection
conn = pymysql.connect(host='localhost', user='python', password='1111!',
                       db='python', charset='utf8')

# pymysql 버전확인
# print(pymysql.__version__)

# 데이터베이스 선택
conn.select_db('python')

# cursor연결
c = conn.cursor()
# print(type(c))

# 데이터 베이스 생성
# c.execute('create database python_app2')

# # 커서 반환
# c.close()
#
# # 접속 해제
# conn.close()

# 날짜 생성
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# c.execute('CREATE TABLE IF NOT EXISTS users (id bigint(20) NOT NULL, \
#           username varchar(20), \
#           email varchar(30), \
#           website varchar(30), \
#           regdate varchar(20) NOT NULL, PRIMARY KEY(id))')

# conn.commit()


try:
    with conn.cursor() as c:
        #JSON to mysql
        with open('C:\\Users\\User\\workspace\\study-python\\section5\\data\\users.json', 'r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                t = (user['id'], user['username'], user['email'], user['website'], nowDatetime)
                userData.append(t)
            c.executemany('insert into users (id, username, email, website, regdate) values (%s, %s, %s, %s, %s)', userData)
        conn.commit()
finally:
    conn.close()

import sqlite3
import simplejson as json
import datetime

# 디비 생성
conn = sqlite3.connect('C:\\Users\\User\\workspace\\study-python\\section5\\database\\sqlite1.db') # isolation_level=None : AutoCommit
# 메모리 디비 생성
# conn = sqlite3.connect(':memory:')

# 날짜 생성
now = datetime.datetime.now()
print('now ==', now)
nowDatetime = now.strftime('%Y-%d-%d %H:%M:%S')
print('nowDatetime ==', nowDatetime)

# sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

# cursor 연결
c = conn.cursor()
print(type(c))

# 테이블 생성
c.execute('CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, email text, phone text, website text, regdate text)')

# 데이터 삽입
# c.execute("insert into users values(1, 'tony', 'test@test.com', '010-1234-5678', 'test.com', ?)", (nowDatetime,))

userList = (
    (2, 'tony2', 'test@test.com', '010-1234-5678', 'test.com', nowDatetime),
    (3, 'tony3', 'test@test.com', '010-1234-5678', 'test.com', nowDatetime),
    (4, 'tony4', 'test@test.com', '010-1234-5678', 'test.com', nowDatetime)
)

# c.executemany("insert into users (id, username, email, phone, website, regdate) values (?,?,?,?,?,?)", userList)

with open('C:\\Users\\User\\workspace\\study-python\\section5\\data\\users.json', 'r') as infile:
    r = json.loads(infile.read())
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        userData.append(t)
    print(userData)
    print(tuple(userData))
    c.executemany("insert into users (id, username, email, phone, website, regdate) values (?,?,?,?,?,?)", userData)

# print('delete', conn.execute('delete from users').rowcount, 'rows')

conn.commit()
conn.close()

import sqlite3

# 디비 생성
conn = sqlite3.connect('C:\\Users\\User\\workspace\\study-python\\section5\\database\\sqlite1.db') # isolation_level=None : AutoCommit

# 커서 연결
c = conn.cursor()

# 데이터 수정1
c.execute('update users set username = ? where id = ?', ('database', 1))

# 데이터 수정2
c.execute('update users set username = :name where id = :id', {'name': 'bbb', 'id': 2})

# 데이터 수정3
c.execute('update users set username = \'%s\' where id = %s' %('ccc', 3))

# 데이터 삭제1
c.execute('delete from users where id = ?', (4,))

# 데이터 확인
for row in c.execute('select * from users'):
    print(row)

conn.commit()

conn.close()

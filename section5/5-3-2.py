import sqlite3

# 디비 생성
conn = sqlite3.connect('C:\\Users\\User\\workspace\\study-python\\section5\\database\\sqlite1.db') # isolation_level=None : AutoCommit

# 커서 바인딩
c = conn.cursor()

# 데이터 조회 전체
c.execute('select * from users')

# 1개 로우 선택
# print(c.fetchone())

# 지정 로우 선택
# print(c.fetchmany(size=4))

# 전체 로우 선택
# print(c.fetchall())

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('user ->', row)

# 순회2
# for row in c.fetchall():
#     print('user ->', row)

# 순회3
# for row in c.execute('select * from users'):
#     print('user ->', row)

# 조건 조회1
param1 = (1,)
c.execute('select * from users where id=?', param1)
print(c.fetchall())

# 조건 조회2
param2 = 1
c.execute('select * from users where id=\'%s\'' % param2)
print(c.fetchall())

# 조건 조회3
c.execute('select * from users where id=:id', {'id': 1})
print(c.fetchall())

# 조건 조회4
param4 = (1, 4)
c.execute('select * from users where id in (?,?)', param4)
print(c.fetchall())

# 조건 조회5
c.execute('select * from users where id=:id1 or id=:id2', {'id1': 1, 'id2': 4})
print(c.fetchall())

# dump
with conn:
    # dump 출력
    with open('C:\\Users\\User\\workspace\\study-python\\section5\\data\\test.dump', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('dump write complete!')

conn.close()

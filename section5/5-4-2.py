import pymysql

# mysql connection
conn = pymysql.connect(host='localhost', user='python', password='1111!',
                       db='python', charset='utf8')

try:
    with conn.cursor(pymysql.cursors.DictCursor) as c: #(conn.cursor()
        c.execute('select * from users')
        # 1개 로우
        # print(c.fetchone())
        # 선택 지정
        # print(c.fetchmany(3))
        # 전체 로우
        # print(c.fetchall())

        # 순회1
        # c.execute('select * from users order by id asc')
        # rows = c.fetchall()
        # for row in rows:
        #     print('row ->', row)

        # 순회2
        # c.execute('select * from users order by id desc')
        # for row in c.fetchall():
        #     print('row ->', row)

        # 조건 조회1
        param1 = (1,)
        c.execute('select * from users where id = %s', param1)
        print('param1 ->', c.fetchall())

        # 조건 조회2
        param2 = 1
        c.execute('select * from users where id = \'%d\'' %param2)
        print('param2 ->', c.fetchall())

        # 조건 조회3
        param3 = (4, 5)
        c.execute('select * from users where id in (%s, %s)', param3)
        print('param3 ->', c.fetchall())

        # 조건 조회4
        param4 = (4, 5)
        c.execute('select * from users where id in (\'%d\', \'%d\')' % param4)
        print('param4 ->', c.fetchall())

finally:
    conn.close()

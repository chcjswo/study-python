import simplejson as json
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

# 파일 db 생성
db = TinyDB('F:\\workspace\\study-python\\section5\\database\\database.db', default_table='users')

# 메모리 db 생성
# db = TinyDB(storage=MemoryStorage, default_table='users')

# 테이블 선택
users = db.table('users')
todos = db.table('todos')

# users 테이블 출력
for item in users:
    pass
    # print(item['username'], ':', item['phone'])

# todos 테이블 출력
for item in todos:
    pass
    # print(item['title'], ':', item['completed'])

# 연결관계 출력
for item in users:
    pass
    # print('[', item['username'], ']')
    for todo in todos:
        if todo['userId'] == item['id']:
            # print(todo['title'])
            pass

# 쿼릭 객체 사용 조회
Users = Query()
Todos = Query()

# 수정
users.update({'username': 'kim'}, Users.id == 3)

user_3 = users.search(Users.id == 3)
print(user_3)

users.remove(Users.id == 3)
print(users.search(Users.id == 3))

db.close()

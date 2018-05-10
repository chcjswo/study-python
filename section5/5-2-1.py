import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB

# 파일 db 생성
db = TinyDB('F:\\workspace\\study-python\\section5\\database\\database.db', default_table='users')

# 메모리 db 생성
# db = TinyDB(storage=MemoryStorage, default_table='users')

# 테이블 선택
users = db.table('users')
todos = db.table('todos')

# 테이블 데이터 삽입
# users.insert({'name': 'tony', 'email': 'test@test.com'})
# todos.insert({'complete': False, 'name': 'homework'})

# 테이블 전체 데이터 삽입1
with open('F:\\workspace\\study-python\\section5\\data\\users.json', 'r') as infile:
    r = json.loads(infile.read())
    for u in r:
        # print(u)
        users.insert(u)

# 테이블 전체 데이터 삽입2
with open('F:\\workspace\\study-python\\section5\\data\\todos.json', 'r') as infile:
    r = json.loads(infile.read())
    for t in r:
        # print(t)
        todos.insert(t)

# 전체 데이터 출력
print(users.all())
print(todos.all())

# 테이블 목록
print(db.tables())

# 전체 데이터 삭제
# users.purge() # db.purge_table('users')
# todos.purge()

# db.purge_tables()
db.close()

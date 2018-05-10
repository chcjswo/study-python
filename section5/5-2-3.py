import simplejson as json
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage

# 파일 db 생성
db = TinyDB('F:\\workspace\\study-python\\section5\\database\\database.db', default_table='users')

# 메모리 db 생성
# db = TinyDB(storage=MemoryStorage, default_table='users')

# 테이블 선택
users = db.table('users')
todos = db.table('todos')

Users = Query()
Todos = Query()

# users 여러가지 조회 방법
print(users.search(Users.id == 7))
print(users.search(Users['id'] == 7))
print(users.search(where('id') == 7))
print(users.search(where('address')['zipcode'] == '90566-7771'))
print(users.search(where('address').zipcode == '90566-7771'))

print('==============================================================')

# 고급 쿼리
print(users.search(Users.email.exists()))
print(users.search(Users['email'].exists()))

print('==============================================================')

# Not
print('Not', users.search(~(Users.username == 'Antonette')))

# OR
print('OR', users.search((Users.username == 'Antonette') | (Users.username == 'Kamren')))

# and
print('and', users.search((Users.username == 'Antonette') & (Users.id == 2)))

print('==============================================================')

# 기타함수
print('len', len(users))
print('len', len(todos))
print('contains', users.contains(Users.id == 2))
print('count', users.count(Users.id == 2))

db.close()

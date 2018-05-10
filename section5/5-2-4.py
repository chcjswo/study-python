import simplejson as json
from tinydb import TinyDB, Query, where

# 파일 db 생성
db = TinyDB('F:\\workspace\\study-python\\section5\\database\\database1.db')

# db.insert({'name': 'tony', 'email': 'test@test.com'}) # json(dict) {}
# db.insert_multiple([
#     {'name': 'jeon', 'email': 'asfsaf@test.com'},
#     {'name': 'chang', 'email': '333434@test.com'}
# ]) # jsonArray(dict) [{}, {}, {}]

SQL = Query()

el = db.get(SQL.name == 'tony')

print(el)
print(el.doc_id)

# 데이터 수정
db.update({'email': 'toto@gmail.com'}, doc_ids=[1, 3])

# 데이터 수정 및 추가
db.upsert({'email': 'test@naver.com', 'login': True}, SQL.name == 'jeon') # update + insert

# 데이터 삭제
db.remove(doc_ids=[1, 3])

db.close()

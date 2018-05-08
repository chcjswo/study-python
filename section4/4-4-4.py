import urllib.request as req
import simplejson as json

url = 'http://jsonplaceholder.typicode.com/comments'
res = req.urlopen(url).read()

items = json.loads(res)
# print(items)

for item in items:
    print('item ===> ', item['id'], 'postId ===> ', item['postId'], 'name ===> ', item['name'], 'email ===> ', item['email'])

# import urllib.request as req
# import simplejson as json
# import os.path
#
# url = 'http://jsonplaceholder.typicode.com/comments'
# savename = 'C:\\Users\\User\\workspace\\study-python\\section4\\comments.json'
#
# if not os.path.exists(url):
#     req.urlretrieve(url, savename)
#
# items = json.load(open(savename, 'r', encoding='utf-8'))
#
# print(type(items))
# print(items)
#
# for item in items:
#     print(item['id'])

import simplejson as json

# Dict(json) 선언
data = {}
data['people'] = []
data['people'].append({
    'name': 'tony',
    'website': 'dolpic.kr',
    'from': 'korea',
    'grade': [34, 23, 65]
})
data['people'].append({
    'name': 'json',
    'website': 'google.com',
    'from': 'usa',
    'grade': [99, 33, 88]
})
data['people'].append({
    'name': 'jane',
    'website': 'apple.com',
    'from': 'france',
    'grade': [34, 76, 34]
})

# print(data)

# json 파일쓰기(dump)

with open('C:\\Users\\User\\workspace\\study-python\\section4\\member2.json', 'w') as outfile:
    json.dump(data, outfile)

with open('C:\\Users\\User\\workspace\\study-python\\section4\\member2.json', 'r') as infile:
    r = json.load(infile)
    print(type(r))
    print(r)
    print('==========================')
    for p in r['people']:
        print('name === ', p['name'])
        print('website === ', p['website'])
        print('from === ', p['from'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' + str(g)
        print('grade === ', grade.lstrip())
        print(' ')

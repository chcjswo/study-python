import simplejson as json

# Dict(json) 선언
data = {}
data['people'] = []
data['people'].append({
    'name': 'tony',
    'website': 'dolpic.kr',
    'from': 'korea'
})
data['people'].append({
    'name': 'json',
    'website': 'google.com',
    'from': 'usa'
})
data['people'].append({
    'name': 'jane',
    'website': 'apple.com',
    'from': 'france'
})

# print(data)

# Dict(json) -> str

# e = json.dumps(data)
e = json.dumps(data, indent=2)
print(type(e))
print(e)

# str -> Dict(json)

d = json.loads(e)
print(type(d))
print(d)


with open('C:\\Users\\User\\workspace\\study-python\\section4\\member.json', 'w') as outfile:
    outfile.write(e)

with open('C:\\Users\\User\\workspace\\study-python\\section4\\member.json', 'r') as infile:
    r = json.loads(infile.read())
    print('==============')
    print(type(r))
    print(r)
    for p in r['people']:
        print('name === ', p['name'])
        print('website === ', p['website'])
        print('from === ', p['from'])
        print(' ')

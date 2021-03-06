import sys
import io
import requests
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get("http://httpbin.org/stream/20", stream=True)
print(r.text)
print(r.encoding)

if r.encoding is None:
    r.endcoding = 'utf-8'

print(r.encoding)

for line in r.iter_lines(decode_unicode=True):
    # print(line)
    b = json.loads(line) #dict
    for e in b.keys():
        print("key => ", e, "values =>", b[e])


s.close()

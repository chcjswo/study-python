import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

ss = requests.Session()
req = ss.get("https://www.naver.com")
print(req.text)

req = ss.get("http://httpbin.org/cookies", cookies={"from":"myName"})
print(req.text)

url = "http://httpbin.org/get"
headers = {"user-agnet": "pythonApp_1.0.0"}
req = ss.get(url, headers=headers)
print(req.text)

ss.close()

with requests.Session() as s:
    r = s.get("https://www.daum.net")
    print(r.text)

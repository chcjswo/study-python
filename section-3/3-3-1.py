import sys
import io
import requests
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r = requests.get("https://api.github.com/events")
r.raise_for_status()
print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set("name", "tony", domain="httpbin.org", path="/cookies")

r = requests.get("http://httpbin.org/cookies", cookies=jar)
r.raise_for_status()
print(r.text)

r = requests.get("https://github.com", timeout=3)
print(r.text)

r = requests.post("http://httpbin.org/post", data={"name": "tony"}, cookies=jar)
print(r.text)

#dict
payload1 = {
    "key1": "values1",
    "key2": "values2"
}
#tuple
payload2 = (
    ("key1", "values1"),
    ("key2", "values2"),
)
#json
payload3 = {"some": "nice"}
# r = requests.post("http://httpbin.org/post", data=payload2, cookies=jar)
r = requests.post("http://httpbin.org/post", data=json.dumps(payload3))
print(r.text)

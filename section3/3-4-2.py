from bs4 import BeautifulSoup
import requests
import sys
import io
import urllib.parse as rep
import os
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

LOGIN_INFO = {
    "log": "",
    "pwd": "",
    "user-submit": rep.quote_plus("로그인"),
    "user-cookie": 1
}

url = "https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F"

with requests.Session() as s:
    login_req = s.post(url , data=LOGIN_INFO)
    # print(login_req.text)
    # print(login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get("https://www.inflearn.com/members/chcjswo")
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, "html.parser")
        # print(soup.prettify)
        badges = soup.select(".badges > ul > li > a > img")
        # print(article)
        for i, e in enumerate(badges, 1):
            # print(i, e["src"])
            fullFileName = os.path.join("D:/imageDown", str(i) + '.jpg')
            req.urlretrieve(e["src"], fullFileName)

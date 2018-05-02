from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

LOGIN_INFO = {
    "user_id": "",
    "user_pw": ""
}

url = "https://user.ruliweb.com/member/login_proc"

with requests.Session() as s:
    login_req = s.post(url , data=LOGIN_INFO)
    # print(login_req.text)
    # print(login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get("http://bbs.ruliweb.com/market/board/320102/read/115880")
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, "html.parser")
        # print(soup.prettify)
        article = soup.select_one("div.board_main_view").find_all("p")
        # print(article)
        for i in article:
            print(i.string)

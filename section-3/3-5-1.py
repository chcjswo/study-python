from bs4 import BeautifulSoup
import requests
import sys
import io
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

URL = "https://www.wishket.com/accounts/login/"
ua = UserAgent()

with requests.Session() as s:
    s.get(URL)
    # print(s.cookies["csrftoken"])
    LOGIN_INFO = {
        "csrfmiddlewaretoken": s.cookies["csrftoken"],
        "identification": "chcjswo",
        "password": "ckdtlr75",
    }
    # print(s.headers)
    res = s.post(URL, data=LOGIN_INFO, headers={"User-Agent": ua.chrome, "Referer": URL})
    # print(res.text)
    # print(res.headers)
    if res.status_code == 200 and res.ok:
        soup = BeautifulSoup(res.text, "html.parser")
        pList = soup.select("table.table-responsive > tbody > tr")
        # print(pList)
        for i in pList:
            print(i)
            print(i.find("th").string, i.find("td").text)

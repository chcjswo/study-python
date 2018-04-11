from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li")

for i, e in enumerate(top10, 1):
    el = e.select_one(".link_issue")
    href = el.attrs['href']
    text = el.string
    # print(i, e.select_one(".link_issue"))
    print(i, text, href)

# top10 = soup.find_all("a", tabindex="-1")
#
# for i,e in enumerate(top10,1):
#     print(i,e.string)

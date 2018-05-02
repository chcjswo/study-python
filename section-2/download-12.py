from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

searchName = "추천-강좌"
base = "https://www.inflearn.com/"
quote = rep.quote_plus(searchName)
url = base + quote

res = req.urlopen(url)
savePath = "C:\\imageDown\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, "html.parser")

# recommand_list = soup.select("ul.slides")[0]
#
# for i, e in enumerate(recommand_list, 1):
#     with open(savePath + searchName + "_" + str(i) + ".txt", "wt") as f:
#         f.write(e.select_one("h4.block_title > a").string)
#
#     # print(img["data-source"])
#     fullFileName = os.path.join(savePath, savePath + searchName + "_" + str(i) + '.png')
#     # print(fullFileName)
#     req.urlretrieve(e.select_one(".block_media > a > img")["src"], fullFileName)

study = soup.select("ul.slides")[1]
print(study)

print("다운로드 완료")

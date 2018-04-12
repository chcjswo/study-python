from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

searchName = "고양이"
base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
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

img_list = soup.select(".img_area > a.thumb._thumb > img")

for i, img in enumerate(img_list, 1):
    # print(img["data-source"])
    fullFileName = os.path.join(savePath, savePath + searchName + "_" + str(i) + '.jpg')
    # print(fullFileName)
    req.urlretrieve(img["data-source"], fullFileName)

print("다운로드 완료")

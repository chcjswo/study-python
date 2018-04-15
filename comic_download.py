from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

comimcNo = 44
sno = 11425

startTime = time.time()

while comimcNo <= 49:
    base = "http://zangsisi.net/?p=" + str(sno)
    url = base
    res = req.urlopen(url)
    savePath = "D:\\imageDown\\comic\\피안도\\" + str(comimcNo) + "\\"

    try:
        if not (os.path.isdir(savePath)):
            os.makedirs(os.path.join(savePath))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("폴더 만들기 실패")
            raise

    soup = BeautifulSoup(res, "html.parser")

    img_list = soup.select(".contents > p > a")

    for i, e in enumerate(img_list, 1):
        el = e.select_one("img")
        href = el.attrs['src']
        text = el.string
        fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
        print(fullFileName)
        req.urlretrieve(href, fullFileName)

    comimcNo += 1
    sno += 2

print()
print(time.time() - startTime, "다운로드 완료")

import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=1135063000'
xml = req.urlopen(url).read()
# print(xml)
#
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)

# BeautifulSoup 파싱
info = {}
for data in soup.findAll('data'):
    seq = (data['seq'])
    hour = data.find('hour').string
    temp = data.find('temp').string
    weather = hour + '시 ===> ' + temp
    info[seq] = weather

print(info)

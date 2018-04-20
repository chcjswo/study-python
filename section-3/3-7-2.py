import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeMemberExr:
    # 초기화
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI
        self.driver = webdriver.Chrome(
            chrome_options=chrome_options,
            executable_path = "C:/Users/User/workspace/study-python/section-3/webdriver/chrome/chromedriver"
        )
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def getMember(self):
        self.driver.get("https://nid.naver.com/nidlogin.login")
        self.driver.find_element_by_name('id').send_keys('id')
        self.driver.find_element_by_name('pw').send_keys('pw')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.get("http://cafe.naver.com/CafeMemberView.nhn?m=view&clubid=26652445")
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('innerframe')
        # print(self.driver.page_source)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # print(soup.prettify)
        return soup.select('.mem_wrap > .mem_list div.ellipsis.m-tcol-c')

    #회원 리스트 출력 및 저장
    def printMemberList(self, list):
        f = open('C:/memberList.txt', 'wt')
        for i in list:
            f.write(i.string.strip() + '\n')
            print(i.string.strip())
        f.close()

    # 소멸자
    def __del__(self):
        # self.driver.close() # 현재 실행 포커스 된 영력 종료
        self.driver.quit() # selenium 전체 프로그램 종료
        print("종료~~")

# 실행
if __name__ == '__main__':
    # 객체 생성
    a = NcafeMemberExr()
    # 시작시간
    start_time = time.time()
    #프로그램 실행
    a.printMemberList(a.getMember())
    # 종료시간
    print("--- Total %s seconds --- " % (time.time() - start_time))
    # 객체 소멸
    del a

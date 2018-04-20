import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    # 초기화
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI
        self.driver = webdriver.Chrome(
            chrome_options = chrome_options
            # executable_path = "C:/Users/User/workspace/study-python/section-3/webdriver/chrome/chromedriver"
        )
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def writeAttendCheck(self):
        print("writeAttendCheck")
        self.driver.get("https://nid.naver.com/nidlogin.login")
        self.driver.find_element_by_name('id').send_keys('id')
        self.driver.find_element_by_name('pw').send_keys('pw')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get("http://cafe.naver.com/AttendanceView.nhn?search.clubid=26652445&search.menuid=10")
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame("cafe_main")
        self.driver.find_element_by_id("cmtinput").send_keys("반갑습니다.")
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a/img').click()
        time.sleep(3)

    # 소멸자
    def __del__(self):
        # self.driver.close() # 현재 실행 포커스 된 영력 종료
        self.driver.quit() # selenium 전체 프로그램 종료
        print("종료~~")

# 실행
if __name__ == '__main__':
    # 객체 생성
    a = NcafeWriteAtt()
    # 시작시간
    start_time = time.time()
    #프로그램 실행
    a.writeAttendCheck()
    # 종료시간
    print("--- Total %s seconds --- " % (time.time() - start_time))
    # 객체 소멸
    del a

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
            chrome_options = chrome_options,
            # executable_path = "C:/Users/User/workspace/study-python/section-3/webdriver/chrome/chromedriver
        )
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def writeAttendCheck(self):
        self.driver.get("http://www.etorrent.co.kr")
        self.driver.find_element_by_name('mb_id').send_keys('id')
        self.driver.find_element_by_name('mb_password').send_keys('pw')
        self.driver.find_element_by_xpath('//*[@id="outlogin_login_input"]/tbody/tr[2]/td/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.etorrent.co.kr/check/index.php")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="att-btn"]').click()
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

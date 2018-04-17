import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
# chrome_options.add_argument("--headless") #CLI 환경설정

driver = webdriver.Chrome(
    # chrome_options = chrome_options,
    chrome_options = None,
    executable_path = "C:/Users/User/workspace/study-python/section-3/webdriver/chrome/chromedriver"
)
driver.set_window_size(1920, 1280)
driver.implicitly_wait(5)

driver.get("https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F")
time.sleep(5)
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="user_login"]').send_keys('id')
driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys('pw')
driver.find_elements_by_xpath('//*[@id="wp-submit"]').click()

driver.quit()

print("완료~~")

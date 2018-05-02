import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.PhantomJS("C:/Users/User/workspace/study-python/section-3/webdriver/phantomjs/phantomjs")

driver.implicitly_wait(5)

driver.get("https://google.com")
driver.save_screenshot("C:/website1.png")

driver.implicitly_wait(5)

driver.get("https://www.daum.net")
driver.save_screenshot("C:/website2.png")

driver.quit()

print("완료~~")

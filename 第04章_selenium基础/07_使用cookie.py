import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=service)
browser.get("https://www.baidu.com")

# 获取cookie
cookies = browser.get_cookies()
print(cookies)
cookiesMap = {data['name']: data['value'] for data in cookies}
print(cookiesMap)

time.sleep(2)
browser.close()
# 关闭浏览器,释放进程
browser.quit()

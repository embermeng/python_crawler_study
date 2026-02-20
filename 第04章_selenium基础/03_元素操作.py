import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver.exe')
browser = webdriver.Chrome(service=service)

browser.get("https://www.baidu.com")

eles = browser.find_elements(By.XPATH, value='//*[@id="s-top-left"]/a')
for ele in eles:
    # 获取元素文本内容
    print(ele.text)
    # 获取元素属性值
    print(ele.get_attribute('href'))


time.sleep(10)
# 关闭浏览器,释放进程
browser.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver.exe')
browser = webdriver.Chrome(service=service)

browser.get("https://www.baidu.com")

# 单个元素定位：
'''
    通过id定位输入框元素：find_element(by=By.ID, value='标签的id属性名)
    除了id外，还可以通过类名：By.CLASS_NAME、标签名：By.TAG_NAME、CSS选择器：By.CSS_SELECTOR、xpath：By.XPATH等定位元素
'''
inputEle = browser.find_element(By.ID, 'chat-textarea')
# 输入关键字内容sora,并赋值给输入框
inputEle.send_keys("sora")
# 点击搜索按钮
browser.find_element(by=By.ID, value='chat-submit-button').click()

# 多个元素定位：find_elements()
# 两者的区别：
#   find_element：定位的是元素的对象，定位不到报错
#   find_elements：定位的是列表，列表里面存元素对象，如果定位不到则是空的数据

time.sleep(10)
# 关闭浏览器,释放进程
browser.quit()

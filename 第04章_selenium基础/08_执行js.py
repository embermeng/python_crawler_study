import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=service)
browser.get("https://hz.lianjia.com/")

# 我想重开一个窗口查看所有的二手房页面，直接写代码字符串，或者读取js文件为字符串
# js = "window.open('https://hz.lianjia.com/ershoufang/');"
# 执行js代码
# browser.execute_script(js)

# 滚动到下面去，点击按钮打开新的页面，如果点击的按钮不在视口中就会报错
js = 'window.scrollTo(0,1000);'
browser.execute_script(js)
time.sleep(2)

# 然后点击查看更多二手房的按钮
browser.find_element(By.XPATH, '//div[@id="modXiaoqu"]/div/div[1]/p/a').click()

time.sleep(5)
browser.close()
# 关闭浏览器,释放进程
browser.quit()

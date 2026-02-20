import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service('./chromedriver.exe')

# 1.实例化配置对象
opts = Options()
# 2.配置对象开启无头模式
opts.add_argument('--headless')
# 3.配置对象添加无显卡模式，即无图形界面
opts.add_argument('--disable-gpu')

browser = webdriver.Chrome(service=service, options=opts)
browser.get("https://www.baidu.com")

# 查看当前页面url
print(browser.current_url)
# 获取页面标题
print("页面标题：", browser.title)
# 获取渲染后的页面源码
print("页面源码-长度：", len(browser.page_source))
# 获取页面cookie
print("cookie-data", browser.get_cookies())

browser.close()
time.sleep(5)
# 关闭浏览器,释放进程
browser.quit()

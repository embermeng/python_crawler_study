import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 可以不设置浏览器驱动路径，但是加载时间会变长
service = Service('./chromedriver.exe')
browser = webdriver.Chrome(service=service)

browser.get("http://www.baidu.com")

# 打印当前标签页的标题
print(browser.title)
# 打印当前响应对应的URL,之前 http的转换成了 https
print(browser.current_url)
# 打印当前网页的源码长度
print(len(browser.page_source))

# 休息10秒，跳转到豆瓣首页,这里的两秒是等当前页面加载完毕，也就是浏览器转完圈后等待的两秒
time.sleep(2)
browser.get('https://www.douban.com')

# 休息2秒，再返回百度
time.sleep(2)
browser.back()

# 休息2秒，再前进到豆瓣
time.sleep(2)
browser.forward()

# 休息2秒，再刷新页面
time.sleep(2)
browser.refresh()

# 保存当前页面的截屏快照
browser.save_screenshot("./screenshot.png")

# 关闭当前标签页
browser.close()

# 关闭浏览器,释放进程
browser.quit()

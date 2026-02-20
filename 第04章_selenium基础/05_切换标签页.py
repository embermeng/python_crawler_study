import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=service)
browser.get("https://www.baidu.com")

# 在通过 selenium打开一个页面，通过点击链接打开新的标签页时，浏览器实例不会自动切换到新标签页的上下文，需要手动切换
browser.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').click()
# 要获取新打开页面的数据，需要切换上下文
browser.switch_to.window(browser.window_handles[1])
# 注意： 句柄列表，这不能提前申明为变量，因为句柄随着新便签页的打开，这是动态变化的current_windows = driver.window_handles不能这么赋值

print(browser.current_url)
print(browser.window_handles)

time.sleep(10)
browser.close()
# 关闭浏览器,释放进程
browser.quit()

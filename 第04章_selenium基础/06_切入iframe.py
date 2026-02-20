import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=service)
browser.get("https://www.baidu.com")

# 如果所定位的元素是在 iframe 中，那么必须先切入到 iframe 中再对元素进行定位。
# 语法格式：switch_to.frame(frame_element)，frame_element可以是id属性、name、index 以及selenium 的 WebElement 对象
# 假如有以下html：
'''
<html lang="en">
<head>
    <title>iframetest</title>
</head>
<body>
<iframe src="a.html" id="fid" name="fname">
	...
	<div id="test-a">
		<a href="test.com" class="test-a">打开页面</a>
	</div>
	...
</iframe>
</body>
</html>
'''
# 1. 用id来定位
# browser.switch_to.frame('fid')

# 2. 用name来定位
# browser.switch_to.frame('fname')

# 3.用frame的index来定位，第一个是0
# browser.switch_to.frame(0)

# 4.用WebElement对象来定位
# browser.switch_to.frame(browser.find_element(By.XPATH, "//*[@id='fid']"))

# 注：切入到 iframe 中之后，如果想对 iframe 外的元素进行操作，必须先从 iframe 中切出后才能操作元素。
browser.switch_to.default_content()

time.sleep(10)
browser.close()
# 关闭浏览器,释放进程
browser.quit()

import requests

# 爬取百度的页面源代码
url = 'http://www.baidu.com'
response = requests.get(url)
response.encoding = 'utf-8' # 设置编码格式
print(response.text) # 拿到页面源代码

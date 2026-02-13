'''
1. 提取主页面每个电影背后的url地址
    拿到'2026必看热片'那一块的html代码，再提取href
2. 访问子页面，提取到电影的名称及下载地址
    拿到页面源代码
    数据提取
'''

import requests
import re

topUrl = 'https://www.dytt8899.com/'

resp = requests.get(topUrl)
resp.encoding = 'gbk'
# print(resp.text)

# 提取html
reg1 = re.compile(r'2026必看热片.*?<ul>(?P<html>.*?)</ul>', re.S)
res1 = reg1.search(resp.text)
html = res1.group("html")

# 提取href
reg2 = re.compile(r"<li><a href='(?P<href>.*?)' title")
res2 = reg2.finditer(html)

reg3 = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<movieName>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
for item in res2:
    href = item.group('href')
    childUrl = topUrl.strip('/') + href
    childResp = requests.get(childUrl)
    childResp.encoding = 'gbk'

    res3 = reg3.search(childResp.text)
    movieName = res3.group("movieName")
    download = res3.group("download")
    print(movieName, download)
    


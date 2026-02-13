from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href="https://www.dytt8899.com//2/">动作片</a></li>
    <li id="abc"><a href="https://www.dytt8899.com//0/">剧情片</a></li>
    <li><a href="https://www.dytt8899.com//3/">爱情片</a></li>
    <li><a href="https://www.dytt8899.com//1/">喜剧片</a></li>
</ul>
"""

# 1. 初始化BeautifulSoup对象
page = BeautifulSoup(html, 'html.parser')

# 查找某个元素：find('标签名', attrs={'属性': '值'}) ，只会找到一个结果
# li = page.find('li', attrs={'id': 'abc'})
# print(li)
# a = li.find('a')
# print(a.text) # 获取文本
# print(a.get('href')) # 获取属性

# 参数和find()一样，但是找到所有结果
li_list = page.find_all('li')
for li in li_list:
    a = li.find('a')
    text = a.text
    href = a.get('href')
    print(text, href)

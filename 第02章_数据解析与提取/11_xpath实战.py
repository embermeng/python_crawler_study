"""
提取：片名、导演、类型、评分、日期、主演、下载链接
"""
import requests
from lxml import etree
import re

url = 'https://www.dytt8899.com/7/'

resp = requests.get(url)
resp.encoding = 'gbk'
et = etree.HTML(resp.text)
tables = et.xpath('//div[@class="co_content8"]/ul/td/table')
nameReg = re.compile(r'.*?片名:(?P<movieName>.*?) .*?导演:(?P<producerName>.*?) ', re.S)
typeReg = re.compile(r'.*?类型:(?P<type>.*?) ', re.S)
for table in tables:
    nameText = table.xpath('.//tr[4]/td/p[1]/text()')
    nameRes = nameReg.findall(nameText[0])
    movieName = nameRes[0][0]
    producerName = nameRes[0][1]

    typeText = table.xpath('.//tr[4]/td/p[2]/text()')
    typeRes = typeReg.findall(typeText[0])
    typeName = typeRes[0]

    print(f'{movieName},{producerName},{typeName}')

print('爬取完成')
resp.close()
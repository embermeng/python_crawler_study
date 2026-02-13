'''
提取：片名、类型、评分、日期、主演、下载链接

'''
import requests
from lxml import etree

url = 'https://www.dytt8899.com/7/'

resp = requests.get(url)
resp.encoding = 'gbk'

et = etree.HTML(resp.text)
tables = et.xpath('//*[@id="header"]/div/div[3]/div[5]/div[2]/div[2]/div[2]/ul/table')
for table in tables:
    table.xpath('./tbody/')

'''
提取：片名、类型、评分、日期、主演、下载链接

'''
import requests
from lxml import etree

url = 'https://www.dytt8899.com/7/'

resp = requests.get(url)
resp.encoding = 'gbk'

et = etree.HTML(resp.text)
ul = et.xpath('/html/body/div/div'
              '/div[@class="bd2"]'
              '/div[@class="bd3"]'
              '/div[@class="bd3r"]'
              '/div[@class="co_area2"]'
              '/div[@class="co_content8"]/ul')

print(ul)

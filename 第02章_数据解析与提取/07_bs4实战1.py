import requests
from bs4 import BeautifulSoup

file = open('book.csv', 'w', encoding='utf-8')

url = 'https://book.douban.com/chart?subcat=all&icn=index-topchart-popular'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}

resp = requests.get(url, headers=headers)

# 初始化BS对象
page = BeautifulSoup(resp.text, 'html.parser')
ul = page.find('ul', attrs={'class': 'chart-dashed-list'})
bodys = ul.find_all('div', attrs={'class': 'media__body'})
for body in bodys:
    bookName = body.find('h2').text.strip()
    desc = body.find('p', attrs={'class': 'subject-abstract color-gray'}).text.strip()
    rating = body.find('span', attrs={'class': 'font-small fleft'}).text.strip()
    price = body.find('span', attrs={'class': 'buy-info'}).find('a').text.strip()
    file.write(f'{bookName},{desc},{rating},{price}\n')

file.close()
resp.close()
print("数据爬取完成")
import requests
from bs4 import BeautifulSoup

url = 'https://wallhaven.cc/search?q=id%3A146214&sorting=random&ref=fp&seed=Oombut&page=2'

resp = requests.get(url)

mainPage = BeautifulSoup(resp.text, 'html.parser')
aList = mainPage.find_all('a', attrs={'class': 'preview'})
for a in aList:
    href = a.get('href')
    childResp = requests.get(href)
    childPage = BeautifulSoup(childResp.text, 'html.parser')
    wallpaper = childPage.find('img', attrs={'id': 'wallpaper'})
    wallpaperUrl = wallpaper.get('src')
    imgName = wallpaperUrl.split('/')[-1]
    print(f"开始下载图片：{imgName}")
    wallpaperResp = requests.get(wallpaperUrl)
    with open(f'./images/{imgName}', 'wb') as file:
        file.write(wallpaperResp.content)

print('图片下载完成')

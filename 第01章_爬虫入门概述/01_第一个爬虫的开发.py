from urllib.request import urlopen

url = 'https://www.baidu.com'

resp = urlopen(url)
# print(resp.read().decode('utf-8'))
with open('baidu.html', 'w', encoding='utf-8') as file:
    file.write(resp.read().decode('utf-8'))

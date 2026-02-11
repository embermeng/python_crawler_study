import requests

url = 'https://fanyi.baidu.com/sug'

data = {
    "kw": input("请输入文本：")
}

resp = requests.post(url, data=data)
# 直接拿到json数据
print(resp.json()['data'])
import requests

url = "https://movie.douban.com/j/chart/top_list"

data = {
    "type": 5,
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
resp = requests.get(url, params=data, headers=headers)
# print(resp.text)
print(resp.json())
print(resp.request.url)  # 打印请求的url地址
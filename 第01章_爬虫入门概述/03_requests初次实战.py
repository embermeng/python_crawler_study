import requests

content = input("请输入要搜索的内容：")
url = f"http://www.sogou.com/web?query={content}"

headers = {
    # 添加一个请求头信息：User-Agent
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
}
response = requests.get(url,headers=headers)
response.encoding = "utf-8"
# print(response.text)
print(response.request.headers)  # 查看默认请求头信息

with open("test.html", "w", encoding="utf-8") as file:
    file.write(response.text)

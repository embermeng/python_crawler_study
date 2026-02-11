# 思路：
# 1. 先获取豆瓣电影top250的页面源码
# 2. 使用正则表达式提取电影信息（如电影名称、评分、评价人数等）
# 3. 将提取的信息保存到文件中或数据库中

import requests
import re

file = open("top250.csv", "w", encoding="utf-8")

url = "https://movie.douban.com/top250"

# 准备好反爬
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
}

# 编写正则表达式
# re.S 模式：让 . 匹配换行符
reg = re.compile(
    r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p>.*?导演: (?P<producer>.*?)&nbsp;.*?<br>(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',
    re.S,
)

# 如何翻页提取：start = (页数 - 1) * 25，一共有10页
for i in range(10):
    page_url = f"{url}?start={i * 25}&filter="
    print(f"正在提取第{i + 1}页的数据, url: {page_url}")
    resp = requests.get(url, headers=headers)
    # resp.encoding = 'utf-8'  # 设置编码为utf-8，确保中文显示正常
    res = reg.finditer(resp.text)
    for i in res:
        name = i.group("name")
        producer = i.group("producer")
        year = i.group("year").strip()  # 去掉两端的空格
        score = i.group("score")
        num = i.group("num")
        print(f"电影名称: {name}, 导演: {producer}, 上映年份: {year}, 评分: {score}, 评价人数: {num}")
        file.write(f"{name},{producer},{year},{score},{num}\n")

file.close()
resp.close()
print("豆瓣TOP250提取完毕")

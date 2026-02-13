from lxml import etree

html = """
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <link rel="shortcut icon" href="https://wallhaven.cc/favicon.ico" />
        <title>Wallpaper Search: #Wuthering Waves - wallhaven.cc</title>
        <meta name="title" content="Wallpaper Search: #Wuthering Waves" />
    </head>
    <body>
        <form id="searchbar" class="expanded">
            <div id="search-category-checks" class="framed">
                <input
                    type="checkbox"
                    name="general"
                    value="general"
                    id="search-general"
                    checked
                /><label for="search-general">General</label>
                <input
                    type="checkbox"
                    name="anime"
                    value="anime"
                    id="search-anime"
                    checked
                /><label for="search-anime">Anime</label>
            </div>
        </form>
        <ul>
            <li><a href="baidu" target="_blank">百度</a></li>
            <li><a href="google" target="_blank">谷歌</a></li>
            <li><a href="bing" target="_blank">必应</a></li>
        </ul>
        <ol>
            <li><a href="feiji" target="_blank">飞机</a></li>
            <li><a href="dapao" target="_blank">大炮</a></li>
            <li><a href="huoche" target="_blank">火车</a></li>
        </ol>
    </body>
</html>
"""
# xpath处理html
et = etree.HTML(html)
# 找到ul下第一个li
# res = et.xpath("/html/body/ul/li[1]/a/text()")

res = et.xpath("//li")
for li in res:
    # ./表示当前节点（li）
    href = li.xpath("./a/@href")[0]
    text = li.xpath("./a/text()")[0]
    print(href, text)
    # 后续的爬虫...


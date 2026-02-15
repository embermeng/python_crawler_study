from pyquery import PyQuery

html = '''
<td height="26">
    <b>
        <a class="ulink1" href='/html/gndy/jddy/'>[综合电影]</a>
        <a href="/i/119075.html" class="ulink2" >2018年国产惊悚片《恐怖浴室》HD国语中字</a>
    </b>
</td>
'''

# PyQuery 和JQuery 一模一样

# 加载html内容
py = PyQuery(html)
# print(py)

# print(py('.ulink'))
# print(py('td b a').text())

# 坑，如果多个标签同时拿属性，只能默认拿到第一个
# print(py('td b a').attr('href'))

# 多个标签拿属性
# gen = py('td b a').items()
# for item in gen:
#     # 拿到属性
#     print(item.attr('href'))
#     # 拿到文本
#     print(item.text())

# div = '''
# <div class="ulink"><span>123</span></div>
# '''
# py = PyQuery(div)
# # html()拿到子元素
# print(py('div').html())
# # text()只拿文本
# print(py('div').text())

# 在标签后添加内容
# py('a.ulink1').after('''<a class="ulink3" href='/123'>123</a>''')

# 在标签内部添加内容
# py('a.ulink1').append('''<span>456</span>''')

# 修改标签属性
# py('a.ulink1').attr('class', 'ulink888')

# 添加标签属性
# py('a.ulink1').attr('id', '888')

# 删除标签属性
# py('a.ulink1').remove_attr('id')

# 删除标签本身
# py('a.ulink1').remove()

# print(py)

# 从多个相同的标签中拿到第一个标签
print(py('b a').eq(0))


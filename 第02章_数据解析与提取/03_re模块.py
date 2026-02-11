import re

# res = re.findall(r"\d+", '我今年18岁，我有999块')
# print(res)

# 这个是重点
# res = re.finditer(r"\d+", "我今年18岁，我有999块")
# print(res)
# for r in res:  # 从迭代器中拿到结果
#     print(r.group())  # group()方法拿到匹配的字符串

# search()方法只会返回第一个匹配的结果
# res = re.search(r"\d+", "我叫周杰伦，今年32岁，班级是5年8班")
# print(res.group())

# match方法从字符串的开头开始匹配，如果开头没有匹配的内容，则返回None，类似再正则前面加了一个^
# res = re.match(r"\d+", "我叫周杰伦，今年32岁，班级是5年8班")
# print(res)

# 预加载正则，提前把正则对象加载完毕
# fileList = []
# reg = re.compile(r'\d+')
# for item in fileList:
#     reg.finditer(item)  # 直接使用预加载的正则对象，不用每次循环都重新创建正则表达式

# 想要提取数据，必须用()括起来，可以单独起名字：(?P<name>正则)
# 提取数据时，需要用group('name')方法提取
s = '''
<div class="西游记"><span id='10086'>中国联通</span></div>
<div class="西游记"><span id='10010'>中国移动</span></div>
'''
reg = re.compile(r"<span id='(?P<id>\d+)'>(?P<content>.*?)</span>")

res = reg.finditer(s)
for item in res:
    print(item.group('id'))
    print(item.group('content'))
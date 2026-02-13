from lxml import etree

# 如果pycharm报错，可以用这种导入方式
# from lxml import html
# etree = html.etree

xml = """
<book>
    <title>Python Web Scraping</title>
    <author>John Doe</author>
    <year>2023</year>
    <price currency="USD">29.99</price>
    <chapters>
        <chapter id="1">Introduction</chapter>
        <chapter id="2">XPath Basics</chapter>
        <chapter id="3">Data Extraction</chapter>
        <div>
            <chapter id="4">atguigu</chapter>
        </div>
    </chapters>
    <abs>
        <chapter id="5">尚硅谷</chapter>
        <chapter id="8">黑马</chapter>
    </abs>
    <chapter id="6">哈哈哈</chapter>
</book>
"""
# xpath处理xml
et = etree.XML(xml)
# /表示根节点，在xpath中间的/是儿子
# res = et.xpath('/book/title/text()')[0]

# 拿到所有后代的标签：//标签名
# res = et.xpath('/book//chapter')

# 拿到book下'*'(谁都行)的chapter，只有chapters和abs的chapter，注意*只能过一层节点，不能过多层
# res = et.xpath('/book/*/chapter/text()')

# 属性筛选：[@属性名='属性值']
# res = et.xpath("/book/chapters/chapter[@id='3']/text()")

# 拿到标签中的属性的值：@属性名，比如：@href
res = et.xpath("/book/abs/chapter/@id")
print(res)




import requests

# 会话
session = requests.session()

# 1. 登录
loginUrl = 'https://pvew5.pver549cn.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=register&frommessage&loginhash=Ld6EX&inajax=1'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
data = {'formhash': '13cf9973', 'referer': 'https://pvew5.pver549cn.com/home.php?mod=spacecp&ac=profile&op=password', 'username': 'embermeng1@outlook.com', 'password': 'ember179.', 'questionid': '0', 'answer': '', 'cookietime': 2592000}
resp = session.post(loginUrl, data=data)
print(resp.text)
# 看下cookie
print(resp.cookies)
# 2. 拿书架的数据
# 上面的session中是有cookie的
pageUrl = ''
resp = session.get(pageUrl, headers=headers)
# 接口返回的json数据
print(resp.json())

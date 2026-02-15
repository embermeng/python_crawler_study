# 代理：使用第三方的机器来代理自己的请求
# 代理的弊端：1. 慢    2. 不好找
import requests

url = 'https://www.baidu.com'

# 准备代理信息
ip = '124.67.20.225'
port = '8090'
proxy = {
    'http': f'http://{ip}:{port}',
    # 'https': f'https://{ip}:{port}',
    'https': None,
}

# 配置代理 proxies
resp = requests.get(url, proxies=proxy)
resp.encoding = 'utf-8'
print(resp.text)

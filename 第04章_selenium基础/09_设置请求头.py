import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_local_proxy():
    from urllib.request import getproxies
    proxy = getproxies()['http']
    # proxies = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}
    proxies = {'http': proxy, 'https': proxy}
    return proxies

p = get_local_proxy()

service = Service('./chromedriver.exe')
opts = Options()
# 设置请求头：add_argument('--请求头=xxxxxx')
# 在options请求头中设置代理
opts.add_argument(f'--proxy-server={p["http"]}')

browser = webdriver.Chrome(service=service, options=opts)
browser.get("https://www.baidu.com/")

time.sleep(5)
browser.close()
# 关闭浏览器,释放进程
browser.quit()

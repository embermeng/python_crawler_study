import asyncio
import aiohttp

urls = [
    'https://w.wallhaven.cc/full/m3/wallhaven-m35gzm.jpg',
    'https://w.wallhaven.cc/full/e8/wallhaven-e8ow3o.jpg',
    'https://w.wallhaven.cc/full/gp/wallhaven-gp3oel.jpg'
]
pixUrls = [
    'https://i.pximg.net/img-original/img/2026/02/07/01/46/30/140859918_p1.png',
    'https://i.pximg.net/img-original/img/2026/01/26/03/01/57/140386890_p0.png',
    'https://i.pximg.net/img-original/img/2025/12/13/01/14/36/138532605_p0.png'
]

headers = {
    'referer': 'https://www.pixiv.net/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
}

# 获取本地代理地址（翻墙用）
def get_local_proxy():
    from urllib.request import getproxies
    proxy = getproxies()['http']
    # proxies = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}
    proxies = {'http': proxy, 'https': proxy}
    return proxies


# 不用 async with：
# async def aio_download(url, session):
#     filename = url.rsplit('/', 1)[1]
#     print('开始下载图片:', filename)
#     resp = await session.get(url)
#     content = await resp.read()
#     print('下载完毕')
#     # 写入文件
#     with open(filename, 'wb') as f:
#         f.write(content)
#
#     # 释放连接
#     await resp.release()

# 用 async with：
async def aio_download(url):
    filename = url.rsplit('/', 1)[1]
    print('开始下载图片:', filename)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, proxy=get_local_proxy()['http']) as resp:
            # 请求回来了，写入文件
            with open(f'./images/{filename}', 'wb') as f:
                f.write(await resp.read())
    print(f'{filename}下载完毕')


async def main():
    tasks = [aio_download(url) for url in pixUrls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

# 章节目录
# 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
# 章节内部的内容
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

import requests
import asyncio
import aiohttp
# 异步读写文件
import aiofiles
from json import dumps
import os

'''
1. 同步操作：访问小说章节目录
2. 异步操作：访问每章的文章内容
'''
os.makedirs('./novel', exist_ok=True)
async def aioDownload(cid, title):
    chapterData = {
        "book_id": bookId, "cid": f"{bookId}|{cid}", "need_bookinfo": 1
    }
    chapterDataStr = dumps(chapterData)
    chapterUrl = f'https://dushu.baidu.com/api/pc/getChapterContent?data={chapterDataStr}'
    async with aiohttp.ClientSession() as session:
        async with session.get(chapterUrl) as resp:
            res = await resp.json()
            content = res['data']['novel']['content']
            async with aiofiles.open(f'./novel/{title}.txt', 'w', encoding='utf-8') as file:
                await file.write(content)
                print(f'{title}下载完毕')


async def getCatalog(url):
    resp = requests.get(url)
    cataList = resp.json()['data']['novel']['items']
    # 准备异步任务
    tasks = [aioDownload(item['cid'], item['title']) for item in cataList]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    bookId = '4306063500'
    catalogData = {"book_id": bookId}
    catalogUrl = f'https://dushu.baidu.com/api/pc/getCatalog?data={dumps(catalogData)}'
    asyncio.run(getCatalog(catalogUrl))

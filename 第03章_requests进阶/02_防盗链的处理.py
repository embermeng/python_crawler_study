import requests

# 拉取视频的网址
url = 'https://www.pearvideo.com/video_1804795'
contId = url.split('_')[1]

videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.1939461099148435'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 防盗链：溯源，本次请求的上一级是谁
    'referer': url,
}
resp = requests.get(videoStatusUrl, headers=headers)
srcUrl = resp.json()['videoInfo']['videos']['srcUrl']
systemTime = resp.json()['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')

# 下载视频
with open('test.mp4', 'wb') as f:
    f.write(requests.get(srcUrl).content)

print('视频下载完毕')
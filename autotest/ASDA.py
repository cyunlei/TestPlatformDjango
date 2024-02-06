import requests



url='https://m3u8.48cdn.com/newhd/202112/61acdbbc394d9220425c53d1/hls/index2.ts'

response=requests.get(url)
with open('./product','wb+') as f:
    f.write(response.content)
    f.flush()
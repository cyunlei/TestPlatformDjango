import requests
from tqdm import tqdm
import re
import json
import os


headers = {
    'cookie': 'VISITOR_INFO1_LIVE=9qZVrzB27uI; PREF=f4=4000000&tz=Asia.Shanghai; _ga=GA1.2.621834420.1648121145; _gcl_au=1.1.1853038046.1648121145; NID=511=Zc1APdmEbCD-iqVNVgI_vD_0S3LVI3XSfl-wUZEvvMU2MLePFKsQCaKUlUtchHSg-kWEVMGOhWUbxpQMwHeIuLjhxaslwniMh1OsjVfmOeTfhpwcRYpMgqpZtNQ7qQApY21xEObCvIez6DCMbjRhRQ5P7siOD3X87QX0CFyUxmY; OTZ=6430350_24_24__24_; GPS=1; YSC=0E115KqM_-I; GOOGLE_ABUSE_EXEMPTION=ID=d02004902c3d0f4d:TM=1648620854:C=r:IP=47.57.243.77-:S=YmZXPW7dxbu83bDuauEpXpE; CONSISTENCY=AGDxDeNysJ2boEmzRP4v6cwgg4NsdN4-FYQKHCGhA0AeW1QjFIU1Ejq1j8l6lwAc6c-pYTJiSaQItZ1M6QeI1pQ3wictnWXTOZ6_y8EKlt0Y_JdakwW6srR39-NLuPgSgXrXwtS0XTUGXpdnt4k3JjQ',
    'referer': 'https://www.youtube.com/results?search_query=jk%E7%BE%8E%E5%A5%B3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
url = 'https://www.youtube.com/watch?v=-305cjg11Wc'
response = requests.get(url=url, headers=headers)

json_str = re.findall('var ytInitialPlayerResponse = (.*?);var', response.text)[0]
json_data = json.loads(json_str)
# print(json_data)
# with open('a.txt','a+') as f:
#     f.write(str(json_data)
video_url = json_data['streamingData']['adaptiveFormats'][0]['url']
url='https://rr1---sn-i3b7knzl.googlevideo.com/videoplayback%3Fexpire%3D1686777283%26ei%3DY9mJZIL0GNeIiga1rJyoBw%26ip%3D8.212.40.201%26id%3Do-AB2OoPzQtMC9C1U0W0FLAYp-tsaH5z2NLVf3LMbW0hDA%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DcX%26mm%3D31%252C29%26mn%3Dsn-i3b7knzl%252Csn-i3belnlz%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D1%26pl%3D18%26ctier%3DSH%26initcwndbps%3D677500%26spc%3DqEK7BwgICnnUru2RR7LkfaqPmaaCCO4%26vprv%3D1%26svpuc%3D1%26mime%3Dvideo%252Fmp4%26ns%3DmLVJCklvhwqGMsgERG-i20sN%26cnr%3D14%26ratebypass%3Dyes%26dur%3D59.953%26lmt%3D1672518260195334%26mt%3D1686755367%26fvip%3D2%26fexp%3D24007246%252C24362685%252C51000013%252C51000022%26c%3DWEB%26txp%3D4530434%26n%3DiT9wBqahIkAcv3URY7%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cctier%252Cspc%252Cvprv%252Csvpuc%252Cmime%252Cns%252Ccnr%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgIg2B-wOBt-9c6kub3DmALYIuVrh_19ow13cv4j2lD1cCIFi0OQjIdaTPDDk2ezyW3WL3nkCduKe2RiamjMv4UxWe'
audio_url = json_data['streamingData']['adaptiveFormats'][-2]['url']
title = json_data['videoDetails']['title']
title = title.replace(' ', '')
title = re.sub(r'[\/:|?*"<>]', '', title)
print('=======================')
print(video_url)
print('=======================')
print(audio_url)
print('==================')
print(title)

video = requests.get(video_url, stream=True)
file_size = int(video.headers.get('Content-Length'))
video_pbar = tqdm(total=file_size)
#
# with open(f'{title}.mp4', mode='wb') as f:
#     # 把视频分成 1024 * 1024 * 2 为等分的大小 进行遍历
#     for video_chunk in video.iter_content(1024*1024*2):
#         # 写入数据
#         f.write(video_chunk)
#         # 更新进度条
#         video_pbar.set_description(f'正在下载{title}视频中......')
#         # 更新进度条长度
#         video_pbar.update(1024*1024*2)
#     # 下载完毕
#     video_pbar.set_description('下载完成！')
#     # 关闭进度条
#     video_pbar.close()

# audio = requests.get(audio_url, stream=True)
# file_size = int(audio.headers.get('Content-Length'))
# audio_pbar = tqdm(total=file_size)
# with open(f'{title}.mp3', mode='wb') as f:
#     for audio_chunk in audio.iter_content(1024*1024*2):
#         f.write(audio_chunk)
#         audio_pbar.set_description(f'正在下载{title}音频中......')
#         audio_pbar.update(1024*1024*2)
#     audio_pbar.set_description('下载完成！')
#     audio_pbar.close()
# import os
# def merge(title):
#     ffmpeg = r'D:\FFmpeg\ffmpeg-2023-06-04-git-b1c3d81e71-full_build\bin\ffmpeg.exe -i 1.mp4 -i 2.mp3 -acodec copy -vcodec copy ' + title + '-out.mp4'
#     os.popen(ffmpeg)
#
# merge('123')
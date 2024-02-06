# import requests
# import time
# import re
# import os
# import threading
# from urllib3.exceptions import InsecureRequestWarning
# import urllib3
#
# urllib3.disable_warnings(InsecureRequestWarning)
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
# }
#
#
# def get_m3u8():
#     ts_url = []
#     url = 'https://m3u8.48cdn.com/newhd/202112/61acdbbc394d9220425c53d1/hls/index.m3u8'
#     response = requests.get(url=url, headers=header)
#     # print(response.text)
#     cop = re.compile(r'index(\d+).ts')
#     find = cop.finditer(response.text)
#     for i in find:
#         url_ts = 'https://m3u8.48cdn.com/newhd/202112/61acdbbc394d9220425c53d1/hls/' + str(i.group(0))
#         ts_url.append(url_ts)
#     return ts_url
#
#
# def threadDownload(start, end, urls):
#     global count
#     count = 0
#     for url in urls[start:end]:
#         try:
#             response = requests.get(url, stream=True, verify=False, headers=header)
#         except Exception as e:
#             print("请求异常：%s" % e.args)
#             exit(0)
#         ts_path = 'D:/data/data_ts/index' + str(count) + '.ts'
#         with open(ts_path, "wb") as file:
#             file.write(response.content)
#         count += 1
#         print("下载进度：%.2f" % (count / len(urls)))
#
#
# def download(urls):
#     num_thread = 100
#     part = 50
#     for i in range(num_thread):
#         start = part * i
#         if i == num_thread - 1:
#             end = len(urls)
#         else:
#             end = start + part
#         t = threading.Thread(target=threadDownload, kwargs={'start': start, 'end': end, 'urls': urls})
#         t.setDaemon(True)
#         t.start()
#
#     main_thread = threading.current_thread()
#     for t in threading.enumerate():
#         if t is main_thread:
#             continue
#         t.join()
#
#
# def combine(files):
#     root_path = 'D:/data/data_mp4/'
#     file_name = "jiangziya.mp4"
#     with open(root_path + file_name, "wb+") as file:
#         for i in range(len(files)):
#             file.write(open(files[i], "rb").read())
#
#     print("合并完成")
#
#
# # 查找文件夹下所有的.ts格式文件
# def fileWalker():
#     root_path = 'D:/data/data_ts/'
#     file_list = []
#     global count
#     count =0
#     for files in os.walk(root_path):
#         # print(files)
#         files[2].sort()
#         count+=1
#         for fn in files[2]:
#             if fn.endswith(str(count)+".ts"):
#                 file_list.append(root_path + "/" + fn)
#
#     return file_list
#
#
# if __name__ == "__main__":
#     print("开始下载......")
#     start = int(time.time())
#     urls = get_m3u8()
#     download(urls)
#     print("下载完成，开始合并ts文件")
#     files = fileWalker()
#     combine(files)
#     end = int(time.time())
#
#     print("下载完成，一共用时：%d" % (end - start))
from lxml import etree
from queue import Queue
import time
import requests
# import gevent
import random
from threading import Thread


# monkey.patch_all()


class m3u8Spider(Thread):
    def __init__(self, url, q, w, e,home_url):
        # 重写写父类的__init__方法
        super(m3u8Spider, self).__init__()
        self.home_url=home_url
        self.url = url
        self.home_q = q
        self.detail_q_title = w
        self.detail_q_ts = e
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }

    def request(self, url):
        file = open('./ip.txt', 'r')
        ip = file.read().split('\n')
        # 请求出错时 重复请求3次
        i = 0
        while i <= 3:
            try:
                print(u"[INFO]请求url:" + url)
                response = requests.get(url=url, headers=self.header, proxies={'http': random.choice(ip)}).content
            except Exception as e:
                print(u'[INFO] %s%s' % (e, url))
            else:
                return response

    def get_home_xpath(self):
        response = self.request(self.url)
        html = etree.HTML(response)
        node_list = html.xpath("//dt[@class='preview-item']")
        for move in node_list:
            detail_url = move.xpath('.//a/@href')
            self.home_q.put(detail_url)

    def get_detail_xpath(self):
        response = self.request(self.home_url)
        html = etree.HTML(response)
        mp4_title = html.xpath('/html/body/div[6]/div/comment()')
        mp4_url = html.xpath('/html/body/div[6]/div/div[2]/div[5]/div[1]/a/@href')
        self.detail_q_title.put(mp4_title)
        self.detail_q_ts.put(mp4_url)

    def download_mp4(self):
        mp4_url = self.detail_q_ts.get()
        mp4_title = self.detail_q_title.get()
        response = self.request(mp4_url)
        print('开始下载：', mp4_title)
        path = 'D:/data/data_mp4/' + mp4_title + '.mp4'
        with open(path, 'wb') as f:
            f.write(response)
            f.flush()

    def run(self):
        self.get_home_xpath()
        self.get_detail_xpath()
        self.download_mp4()


def main():
    q = Queue()
    w = Queue()
    e = Queue()
    base_url = 'https://www.b4c44.com/movie/gaoqing/index_{}.html'
    # 构造所有url
    url_list = [base_url.format(str(num)) for num in range(2, 4 + 1, 1)]
    home_url_q = e.get()
    home_url = 'https://www.b4c44.com' + home_url_q
    # 创建协程并执行
    # 保存线程
    Thread_list = []
    # 创建并启动线程
    for url in url_list:
        p = m3u8Spider(url, q, w, e,home_url)
        p.start()
        Thread_list.append(p)

    # 让主线程等待子线程执行完成
    for i in Thread_list:
        i.join()

    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    start = time.time()
    main()
    print('[info]耗时：%s' % (time.time() - start))

import requests
import time

#
# url='http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=99ef147c18214cb5aac0133a5aa3c719&orderno=YZ20223310703mixqrk&returnType=2&count=20'
# response=requests.get(url)
# km=[]
# for s in range(50):
#     time.sleep(6)
#     for i in response.json()['RESULT']:
#         # print(i)
#         ip_address='http://'+i['ip']+':'+i['port']
#         km.append(ip_address)
#
# for m in list(set(km)):
#     with open('./ip.txt','a+') as f:
#         f.write(m+'\n')
#         f.flush()

# file = open('./ip.txt', 'r')
# a = file.read()
# print(a.split('\n'))

base_url = 'https://www.b4c44.com/movie/gaoqing/index_{}.html'
url_list = [base_url.format(str(num)) for num in range(2, 71 + 1, 1)]
print(url_list)

import requests
import time
import re
response=requests.get('https://m3u8.38cdn.com/newhd/202105/608dc6feeaff61400b6b888f/m3u8/index.m3u8')
req=response.text

if req is '.ts':
    print(req)
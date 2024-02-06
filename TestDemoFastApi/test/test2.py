import time
from random import randint
import redis




def set_code():
    vs = {}
    times = round(time.time())
    s = 5 * 60
    vs_code = randint(100000, 999999)
    r=redis.Redis(host='localhost',port=6379,db=0)
    vtime=times+s
    vt=str(vs_code)+'.'+str(vtime)
    # print(vt)
    r.set('cyunlei9@163.com',vt)

def get_code():
    r = redis.Redis(host='localhost', port=6379, db=0)
    s=r.get('cyunlei9@163.com')
    ut=str(s).split('.')
    print(int(ut[0].strip("b'")))
    print(int(ut[1].strip("'")))

# set_code()
get_code()
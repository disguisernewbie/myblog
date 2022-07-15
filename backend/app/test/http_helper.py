import requests
import json
from ctypes import *


data = {
        'datetime': '2021-10-27',
        'type': '登录回报',
        'msg': '结构体',
}
if __name__ == '__main__':
    r = requests.get('http://192.168.2.4:8002/user/guser/')
    print(r.text)
    
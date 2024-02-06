from api.ParseFile import LoginUser
import os
from common.read_data import data
from api.ParseFile import lu


class LoginUserParse():
    """
    解析读取case文件，构造请求
    """

    def __init__(self):
        pass

    def login(self, **kwargs):
        return lu.request(method=lu.model_method, url=lu.model_url, headers=lu.model_headers,
                          data=lu.model_data, **kwargs)


lup = LoginUserParse()

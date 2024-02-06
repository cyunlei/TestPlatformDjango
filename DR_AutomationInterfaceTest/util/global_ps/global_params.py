class GlobalParams:
    # 定义一个项目全局变量的类

    def __init__(self):
        # 定义全局变量
        self._global_dict = {}

    def set_token(self, u_token):
        # 设置token
        self._global_dict['u_token'] = u_token
        return self._global_dict

    def get_token(self,key):
        # 获取token
        try:
            return self._global_dict[key]
        except KeyError:
            return None


GP = GlobalParams()

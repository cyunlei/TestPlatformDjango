import datetime


class Time:
    def current_time(self):
        # 获取当前时间戳
        timestamp = datetime.datetime.now().timestamp()

        # 格式化时间戳
        formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        return formatted_timestamp


time=Time()
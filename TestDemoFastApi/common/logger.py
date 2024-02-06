import logging, time, os
import logging.handlers

# 获取当前项目的根目录
BASH_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 定义日志文件路径
LOG_PATH = os.path.join(BASH_PATH, 'logs')

# 判断当前log目录路径是否存在，不存在则创建
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():
    def __init__(self, module_name='api'):

        # 定义日志文件的名字，格式为：模块名-年-月-日.log
        self.logname = os.path.join(LOG_PATH, "{}-{}.log".format(module_name, time.strftime("%Y-%m-%d")))

        # 获取名为'log'的日志记录器实例。如果这个记录器不存在，将会创建一个。
        self.logger = logging.getLogger('log')

        # 定义日志的格式。这里使用了特定的格式字符串，包括时间、文件名、行号、日志级别和消息内容。
        self.formater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        # 创建一个新的文件处理器，用于将日志写入到指定的文件。这里指定了文件名（通过self.logname获得），模式为追加模式，并且编码方式为UTF-8
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")

        # 创建一个RotatingFileHandler实例，用于按文件大小轮换日志文件。这里定义了每个日志文件的最大大小为10MB，最多保留5个日志文件。
        self.RotatingFileHandler = logging.handlers.RotatingFileHandler(self.logname, maxBytes=1024 * 1024 * 10,
                                                                        backupCount=5)
        
        # 创建一个TimedRotatingFileHandler实例，用于按时间轮换日志文件。这里定义了每天轮换一次，并保留最近7天的日志文件。
        self.TimedRotatingFileHandler = logging.handlers.TimedRotatingFileHandler(self.logname, when='D',
                                                                                  backupCount=30)

        # 创建一个新的控制台处理器，用于将日志输出到控制台
        self.console = logging.StreamHandler()

        # 设置控制台处理器记录的日志级别为DEBUG
        self.console.setLevel(logging.DEBUG)

        # 设置文件处理器记录的日志级别为DEBUG
        self.filelogger.setLevel(logging.DEBUG)

        # 为文件处理器和控制台处理器设置日志格式。这里使用了之前定义的formater。
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)

        # 将文件处理器和控制台处理器添加到日志记录器中，这样当记录器记录日志时，这些处理器就会接收到并处理这些日志。
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

        # 将之前定义的RotatingFileHandler和TimedRotatingFileHandler也添加到日志记录器中
        self.logger.addHandler(self.RotatingFileHandler)
        self.logger.addHandler(self.TimedRotatingFileHandler)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.debug("---测试结束---")

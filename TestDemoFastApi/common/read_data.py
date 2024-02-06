import yaml
import json
from configparser import ConfigParser
from common.logger import logger
import os


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        """
        读取yaml文件
        :param file_path: yaml文件路径
        :return: yaml文件内容
        """
        try:
            logger.info('读取yaml文件：{} ......'.format(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            logger.info('读到数据 ======>>>>>>  {} '.format(data))
            return data
        except Exception as e:
            logger.error('读取yaml文件失败，原因是：{}'.format(e))

    def load_json(self, file_path):
        """
        读取json文件
        :param file_path: json文件路径
        :return: json文件内容
        """
        try:
            logger.info('读取json文件：{} ......'.format(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info('读到数据 ======>>>>>>  {} '.format(data))
            return data
        except Exception as e:
            logger.error('读取json文件失败，原因是：{}'.format(e))

    def load_ini(self, file_path):
        """
        读取ini文件
        :param file_path: ini文件路径
        :return: ini文件内容
        """
        try:
            logger.info('读取ini文件：{} ......'.format(file_path))
            config = MyConfigParser()
            config.read(file_path, encoding='utf-8')
            data = dict(config._sections)
            logger.info('读到数据 ======>>>>>>  {} '.format(data))
            return data
        except Exception as e:
            logger.error('读取ini文件失败，原因是：{}'.format(e))

    def load_file(self, file_path, isList=False):
        """
        读取文件
        :param isList: 是否以列表形式返回
        :param file_path: 文件路径
        :return: 文件内容
        """
        try:
            logger.info('读取文件：{} ......'.format(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                data = f.read()
            logger.info('读到数据 ======>>>>>>  {} '.format(data))
            if isList:
                return data.split('\n')
            return data
        except Exception as e:
            logger.error('读取文件失败，原因是：{}'.format(e))

    def load_csv(self, file_path):
        """
        读取csv文件
        :param file_path: csv文件路径
        :return: csv文件内容
        """

        try:
            logger.info('读取csv文件：{} ......'.format(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                data = f.read()
            logger.info('读到数据 ======>>>>>>  {} '.format(data))
            return data.split('\n')
        except Exception as e:
            logger.error('读取csv文件失败，原因是：{}'.format(e))

    def load_xlsx(self, file_path):
        """
        读取xlsx文件
        :param file_path: xlsx文件路径
        :return: xlsx文件内容
        """
        try:
            logger.info('读取xlsx文件：{} ......'.format(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                data = f.read()
            logger.info('读到数据 ======>>>>>>  {} '.format(data))
            return data
        except Exception as e:
            logger.error('读取xlsx文件失败，原因是：{}'.format(e))

    def load_xls(self, file_path):
        """
        读取xls文件
        :param file_path: xls文件路径
        :return: xls文件内容
        """
        try:
            logger.info('读取xls文件：{} ......'.format(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                data = f.read()
            logger.info('读到数据 ======>>>>>>  {} '.format(data))
            return data
        except Exception as e:
            logger.error('读取xls文件失败，原因是：{}'.format(e))


data = ReadFileData()


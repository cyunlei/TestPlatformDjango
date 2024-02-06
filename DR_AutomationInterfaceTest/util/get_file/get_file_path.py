from common.logger import logger
import re


def categorize_files(filelist):
    categories = {}  # 存储每个分类的文件列表
    for file in filelist:
        # 提取文件名的分类部分
        if '_' in file:
            category = file.split('_')[0]
            # 如果分类在字典中不存在，则创建一个空列表
            if category not in categories:
                categories[category] = []
                # 将文件添加到相应的分类列表中
            categories[category].append(file)

        else:
            category_1 = re.sub(r'\d+', '', file.strip().split('.')[0])
            if category_1 not in categories:
                categories[category_1] = []
            categories[category_1].append(file)

    return categories


def file_classify(file_path_name):
    """
    文件分类
    :return:
    """
    yaml_file_name = []
    json_file_name = []
    csv_file_name = []
    xlsx_file_name = []
    txt_file_name = []
    file_classify_list = []
    if file_path_name:
        for file_name in file_path_name:
            if file_name.endswith('.yml'):
                yaml_file_name.append(file_name)
            if file_name.endswith('.json'):
                json_file_name.append(file_name)
            if file_name.endswith('.csv'):
                csv_file_name.append(file_name)
            if file_name.endswith('.xlsx'):
                xlsx_file_name.append(file_name)
            if file_name.endswith('.txt'):
                txt_file_name.append(file_name)
    else:
        logger.error('==============数据文件夹为空======================')
    for file_list in [yaml_file_name, json_file_name, csv_file_name, xlsx_file_name, txt_file_name]:
        file_classify_list.append(categorize_files(file_list))
    return file_classify_list


def get_data(filename='', BASE_PATH=None):
    """
    获取数据文件
    :param yaml_path_filename:
    :return:
    """
    file_name_path = file_classify(BASE_PATH)
    logger.info('==================获取数据文件====================')
    logger.info('=================={}===================='.format(file_name_path))
    for file_name in file_name_path:
        if filename in file_name:
            if file_name[filename]:
                return file_name[filename]

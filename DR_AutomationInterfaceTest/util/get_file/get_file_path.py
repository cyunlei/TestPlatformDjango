from common.logger import logger
import re


def categorize_files(filelist):
    categories = {}  # �洢ÿ��������ļ��б�
    for file in filelist:
        # ��ȡ�ļ����ķ��ಿ��
        if '_' in file:
            category = file.split('_')[0]
            # ����������ֵ��в����ڣ��򴴽�һ�����б�
            if category not in categories:
                categories[category] = []
                # ���ļ���ӵ���Ӧ�ķ����б���
            categories[category].append(file)

        else:
            category_1 = re.sub(r'\d+', '', file.strip().split('.')[0])
            if category_1 not in categories:
                categories[category_1] = []
            categories[category_1].append(file)

    return categories


def file_classify(file_path_name):
    """
    �ļ�����
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
        logger.error('==============�����ļ���Ϊ��======================')
    for file_list in [yaml_file_name, json_file_name, csv_file_name, xlsx_file_name, txt_file_name]:
        file_classify_list.append(categorize_files(file_list))
    return file_classify_list


def get_data(filename='', BASE_PATH=None):
    """
    ��ȡ�����ļ�
    :param yaml_path_filename:
    :return:
    """
    file_name_path = file_classify(BASE_PATH)
    logger.info('==================��ȡ�����ļ�====================')
    logger.info('=================={}===================='.format(file_name_path))
    for file_name in file_name_path:
        if filename in file_name:
            if file_name[filename]:
                return file_name[filename]

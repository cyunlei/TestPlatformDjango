import random
import datetime
from common.mysql_common import db

phone_brand = ['小米', '华为', '苹果', '三星', 'OPPO', 'VIVO', '魅族', '一加', '诺基亚', '中兴', '联想', '索尼', '努比亚', '360', '锤子', '金立',
               '美图', '黑鲨', '红米', '荣耀', '乐视', 'HTC', '摩托罗拉', '飞利浦', '海信', '夏普', '谷歌', 'LG', '小辣椒', '360', 'TCL', '酷派',
               '朵唯', '优米', '语信', '奇酷', '酷比']

phone_modelNumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                     'max', 'max pro', 'max plus', '青春版']
phone_size_l = ['5.5', '5.8', '6.0', '6.2', '6.4', '6.5', '6.7', '6.8', '7.0', '7.2', '7.5', '7.8', '8.0', '8.2', '8.5',
                '8.8', '9.0', '9.2', '9.5', '9.8', '10.0']
phone_color_l = ['黑色', '白色', '红色', '蓝色', '绿色', '黄色', '紫色', '橙色', '灰色', '粉色', '青色', '棕色', '金色', '银色', '透明色', '双色', '多色']
phone_system_l = ['安卓', '苹果', '鸿蒙', '微软', '谷歌', '三星', '诺基亚', '索尼', '中兴', '联想', 'OPPO', 'VIVO', '魅族', '一加', '努比亚', '360',
                  '锤子', '金立', '美图', '黑鲨', '红米', '荣耀', '乐视', 'HTC', '摩托罗拉', '飞利浦', '海信', '夏普', 'LG', '小辣椒', 'TCL', '酷派',
                  '朵唯', '优米', '语信', '奇酷', '酷比']


def get_phone_brand():
    phone_name = random.choice(phone_brand) + random.choice(phone_modelNumber)
    phone_price = random.randint(1000, 10000)
    phone_number = random.randint(10, 1000)
    phone_size = random.choice(phone_size_l)
    phone_color = random.choice(phone_color_l)
    phone_system = random.choice(phone_system_l)
    start_year = 2000
    end_year = 2030
    random_datetime = datetime.datetime(  # 生成一个指定范围内的随机日期
        year=random.randint(start_year, end_year),
        month=random.randint(1, 12),
        day=random.randint(1, 28),  # 请根据实际情况调整，考虑每个月的天数
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )
    phone_putaway_time = random_datetime.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期
    is_delete = random.randint(0, 1)  # 0 未删除 1 已删除
    is_putaway = 1  # 0 未上架 1 已上架
    if is_delete == 1:
        is_putaway = 0

    return phone_name, phone_size, phone_color, phone_system, phone_price, phone_number, phone_putaway_time, is_delete, is_putaway


for i in range(1000):
    hone_name, phone_size, phone_color, phone_system, phone_price, phone_number, phone_putaway_time, is_delete, is_putaway = get_phone_brand()
    db.execute_db(
        "insert into cxx_product (product_name,product_size,product_color,product_system,product_price,phone_number,phone_putaway_time,product_is_delete,product_is_putaway) values"
        "('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % ( hone_name, phone_size, phone_color, phone_system, phone_price, phone_number, phone_putaway_time, is_delete, is_putaway))

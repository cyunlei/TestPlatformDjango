import os
import random
from PIL import Image, ImageDraw, ImageFilter

# 定义保存随机生成的马赛克图片的目录
SAVE_PATH = 'data/mosaic'


def random_mosaic(img_path, size_range=(50, 300), count_range=(50, 200)):
    """
    随机生成马赛克图片

    Args:
        img_path: 原始图片路径
        size_range: 马赛克大小范围，默认为 (50, 300)
        count_range: 马赛克数量范围，默认为 (50, 200)

    Returns:
        None
    """
    try:
        # 读取原始图片
        with Image.open(img_path) as img:
            # 获取图片大小
            width, height = img.size
            # 生成马赛克数量和大小
            size_min, size_max = size_range
            count_min, count_max = count_range
            mosaic_count = random.randint(count_min, count_max)
            mosaic_sizes = [random.randint(size_min, size_max) for _ in range(mosaic_count)]
            # 生成马赛克图片
            for i in range(mosaic_count):
                # 随机生成马赛克宽高和左上角坐标
                mosaic_size = mosaic_sizes[i]
                x1 = random.randint(0, width - mosaic_size)
                y1 = random.randint(0, height - mosaic_size)
                x2 = x1 + mosaic_size
                y2 = y1 + mosaic_size
                # 将区域内的像素块变为马赛克
                mosaic = img.crop((x1, y1, x2, y2)).resize((10, 10), Image.ANTIALIAS).resize((mosaic_size, mosaic_size),
                                                                                             Image.ANTIALIAS)
                # 将马赛克图片保存到文件
                filename = os.path.basename(img_path).split('.')[0] + '_mosaic_' + str(i) + '.jpg'
                mosaic.save(os.path.join(SAVE_PATH, filename))
    except Exception as e:
        print(f'Error: {e}')


def mosaic_generation():
    """
    生成马赛克图片

    Returns:
        None
    """
    # 遍历 data/original 目录下的所有图片文件
    for filename in os.listdir('data/original'):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            file_path = os.path.join('data/original', filename)
            # 随机生成马赛克并保存
            random_mosaic(file_path)
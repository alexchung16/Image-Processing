# !_*_ coding:utf8 _*_
# @function 图像扩增
# @Author alexchung
# @Date 20/8/2019 14:13 PM

import os
import numpy as np
import random
import cv2 as cv
from expend_image import MultipleProcessingImage


def mkdirCheck(path):
    """
    创建目录
    os.path.exists(path) 判断一个目录是否存在
    os.makedirs(path) 多层创建目录
    os.mkdir(path) 创建目录
    :param path:
    :return:
    """
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 如果不存在
    if os.path.exists(path):
        print(path, '已经存在')
    else:
        os.makedirs(path)
        print(path, '已经成功创建')


if __name__ == "__main__":
    random_index = random.sample((np.arange(3).tolist()), 2)

    path = os.path.abspath('..\\..') + '\databases\\fruit_vegetables\\watermelon'
    # cv.imshow('image', img)
    # cv.waitKey(0)
    new_path = os.path.abspath('..\\..') + '\databases\\fruit_vegetables\\new_watermelon'

    process = MultipleProcessingImage(src_path=path, dst_path=new_path, category_name='watermelon')
    process.run()







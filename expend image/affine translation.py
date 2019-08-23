# !_*_ coding:utf8 _*_
# @function 平移变换
# @Author alexchung
# @Date 23/8/2019 14:46 PM

import os
import numpy as np
import random
import cv2 as cv


def roiImage(src_img, rect):
    """
    提取感兴趣区域（Region Of Interest, ROI）
    :param img: 源图像
    :param rect: 感兴趣区域信息
    :return:
    """
    x, y, w, h = rect
    # 存储三通道信息
    roi_img = src_img[int(y):int(y+h), int(x):int(x+w)]
    return roi_img


def translationImage(src_img, trans_rate=0.2, direction=3):
    """
    图像平移
    :param img: 源图像
    :param trans_rate: 平移比率
    :param direction: 移动方向 0：左上， 1：右上 2：左下 3：右下 4：随机方向
    :return: 目标图像
    """
    # 控制平移方向
    direction_x = 1
    direction_y = 1

    roi_weight = src_img.shape[0] * (1 - trans_rate)
    roi_height = src_img.shape[1] * (1 - trans_rate)

    rect_info = (0, 0, src_img.shape[0], src_img.shape[1])
    # 选择平移方向
    if direction == 0:
        direction_x, direction_y = (-1, -1)
    elif direction == 1:
        direction_x, direction_y = (1, -1)
    elif direction == 2:
        direction_x, direction_y = (-1, 1)
        rect_info = (0, src_img.shape[1] * trans_rate, roi_weight, roi_height)
    elif direction == 3:
        direction_x, direction_y = (1, 1)
        rect_info = (src_img.shape[0] * trans_rate, src_img.shape[1] * trans_rate, roi_weight, roi_height)
    elif direction == 4:
        direction_x, direction_y = tuple(random.sample((-1, 1), 2))

    # 选择兴趣区域尺寸
    if (direction_x, direction_y) == (-1, -1):
        rect_info = (0, 0, roi_weight, roi_height)
    elif (direction_x, direction_y) == (1, -1):
        rect_info = (src_img.shape[0] * trans_rate, 0, roi_weight, roi_height)
    elif (direction_x, direction_y) == (-1, 1):
        rect_info = (0, src_img.shape[1] * trans_rate, roi_weight, roi_height)
    elif (direction_x, direction_y) == (1, 1):
        rect_info = (src_img.shape[0] * trans_rate, src_img.shape[1] * trans_rate, roi_weight, roi_height)

    # 平移矢量大小
    distance_x = src_img.shape[0] * trans_rate * direction_x
    distance_y = src_img.shape[1] * trans_rate * direction_y
    # 构建仿射矩阵
    M = np.float32([[1, 0, distance_x], [0, 1, distance_y]])
    # 获取平移图片
    translation_img = cv.warpAffine(src_img, M, (int(src_img.shape[0]), int(src_img.shape[1])))
    # 提取感兴趣区域
    translation_roi_img = roiImage(translation_img, rect_info)
    return translation_roi_img


if __name__ == "__main__":
    path = os.path.abspath('..\\..\\..') + '\\databases\\image'

    img_path = os.path.join(path, 'girl.jpg')
    src_img = cv.imread(img_path)

    trans_img = translationImage(src_img, 0.1, 4)
    cv.imshow('src image', src_img)
    cv.imshow('translation image', trans_img)
    cv.waitKey(0)

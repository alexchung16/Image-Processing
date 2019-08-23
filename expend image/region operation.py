# !_*_ coding:utf8 _*_
# @function 图像区域操作
# @Author alexchung
# @Date 23/8/2019 11:17 AM

import os
import numpy as np
import cv2 as cv


def mkdirCheck(self, path, is_makdir=False):
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

    if is_makdir:
        # 如果不存在
        if os.path.exists(path):
            print(path, '已经存在')
        else:
            os.makedirs(path)
            print(path, '已经成功创建')
    else:
        if os.path.exists(path):
            return True
        else:
            return False

def drawRect(src_img, rect):
    """
    绘制矩形框
    :param img: 源图像
    :param rect: 矩形框坐标信息
    :return:
    """
    x, y, w, h = rect
    # 存储三通道信息
    rect_img = np.zeros((h, w, 3))
    rect_img = cv.rectangle(src_img, (int(x), int(y)), (int(x+w), int(y+h)), (255, 255, 0), 2)
    return rect_img


def roiImage(src_img, rect):
    """
    提取感兴趣区域（Region Of Interest, ROI）
    :param img: 源图像
    :param rect: 感兴趣区域信息
    :return:
    """
    x, y, w, h = rect
    # 存储三通道信息
    roi_img = np.zeros((h, w, 3))
    roi_img = src_img[int(y):int(y+h), int(x):int(x+w)]
    return roi_img


def cutImage(src_img, cut_rating=0.8):
    """
    提取感兴趣区域（Region Of Interest, ROI）
    :param img: 源图像
    :param rect: 感兴趣区域信息
    :return:
    """
    img_w = src_img.shape[0]
    img_h = src_img.shape[1]
    x = np.random.randint(0, img_w*(1-cut_rating))
    y = np.random.randint(0, img_h*(1-cut_rating))
    w = int(img_w*cut_rating)
    h = int(img_h*cut_rating)
    # 存储三通道信息
    roi_img = np.zeros((h, w, 3))
    roi_img = src_img[int(y):int(y + h), int(x):int(x + w)]
    return roi_img


if __name__ == "__main__":

    path = os.path.abspath('..\\..\\..') + '\\databases\\image'
    img_path = os.path.join(path, 'girl.jpg')

    src_img = cv.imread(img_path)
    # HSV(Hue , Saturation , Value):色调，饱和度，明度

    rect = (100, 120, 400, 350)
    rect_img = drawRect(src_img, rect)
    roi_img = roiImage(src_img, rect)
    cut_img = cutImage(src_img)

    cv.imshow('src image', src_img)
    cv.imshow('rect image', rect_img)
    cv.imshow('roi image', roi_img)
    cv.imshow('cut image', cut_img)
    # PIL_image.show()

    cv.waitKey(0)

# !_*_ coding:utf8 _*_
# @function 图像锐化
# @Author alexchung
# @Date 21/8/2019 16:32 PM

import os
import numpy as np
import cv2 as cv


def image_scale(img):
    scale_img = np.zeros(img.shape, np.uint8)
    min_pixel = img[0][0]
    max_pixel = img[0][0]
    for i in range(h):
        for j in range(w):
            if min_pixel > img[i][j]:
                min_pixel = img[i][j]
            if max_pixel < img[i][j]:
                max_pixel = img[i][j]
    for i in range(h):
        for j in range(w):
            scale_img[i][j] = 255 * (img[i][j] - min_pixel) / (max_pixel - min_pixel)
    return scale_img


def laplacian_sharping(img):
    """
    原始图像
    :param img:
    :return:
    """
    # 转换为灰度图像
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    laplace_raw_img = np.zeros(gray_img.shape)
    h = gray_img.shape[0]
    w = gray_img.shape[1]
    # 执行卷积操作
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                laplace_raw_img[i][j] = gray_img[i][j]
            else:
                laplace_raw_img[i][j] = int(gray_img[i - 1, j]) + int(gray_img[i + 1, j]) + int(gray_img[i, j - 1]) \
                                        + int(gray_img[i, j + 1]) - int(4 * gray_img[i, j])
    laplace_dst_img = gray_img + laplace_raw_img
    dst_laplace_img = np.uint8(laplace_dst_img)

    return gray_img, laplace_raw_img, dst_laplace_img


if __name__ == "__main__":

    path = os.path.abspath('..\\..\\..') + '\\databases\\image'
    img_path = os.path.join(path, 'girl.jpg')
    src_img = cv.imread(img_path)

    # opencv库 laplace 运算
    gray_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
    laplace_img = cv.Laplacian(gray_img, ddepth=cv.CV_32F, ksize=3)
    abs_img = cv.convertScaleAbs(laplace_img)

    # method 1
    # 拉普拉斯锐化 调用opencv库
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst_img = cv.filter2D(src_img, -1, kernel=kernel)

    # method 2
    # 自定义拉普拉斯锐化函数
    gray_img, laplace_raw_img, dst_laplace_img = laplacian_sharping(src_img)

    cv.imshow('img', src_img)
    cv.imshow('gray image', gray_img)
    cv.imshow('laplacian', laplace_img)
    cv.imshow('scaleAbs image', abs_img)
    cv.imshow('dst image', dst_img)
    cv.imshow('laplacian raw image', laplace_raw_img)

    cv.imshow('laplacian scale image', dst_laplace_img)
    cv.waitKey(0)



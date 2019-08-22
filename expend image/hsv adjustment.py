# !_*_ coding:utf8 _*_
# @function 饱和度调整
# @Author alexchung
# @Date 22/8/2019 15:44 PM

import os
import numpy as np
import random
import cv2 as cv


def linearStrech(pixel, x0, y0, x1, y1, raw_scale, new_uperscale):
   """
   线性拉伸
   :param pixel:
   :param x0:
   :param y0:
   :param x1:
   :param y1:
   :param raw_scale:
   :param new_scale:
   :return:
   """
   # 拉伸后像素值

   scope0 = (new_uperscale*y0)/(raw_scale*x0)
   scope1 = (new_uperscale*(y1-y0))/(raw_scale*(x1-x0))
   scope2 = (new_uperscale*(1-y1))/(raw_scale*(1-y0))
   if pixel < x0:
       strech_pixel = scope0 * pixel
   elif pixel < x1:
       strech_pixel = new_uperscale*y0 + scope1*(pixel - raw_scale*x0)
   else:
       strech_pixel = new_uperscale*y1 + scope2*(pixel - raw_scale*x1)

   return int(strech_pixel)


def hsv_adjustment(img, upper_hue, upper_saturation, upper_value):
    """
       # HSV(Hue , Saturation , Value):色调，饱和度，明度
    :param img: BGR 图像
    :param upper_hue: 色相 0~180
    :param upper_saturation: 对比度 0~255
    :param upper_value: 明度 0~255
    :return:
    """

    hsv_img = cv.cvtColor(src_img, cv.COLOR_BGR2HSV)

    # cv.waitKey(0)
    dst_hsv_img = np.zeros(hsv_img.shape, dtype=np.uint8)
    # 定义
    mask = np.zeros(hsv_img.shape, dtype=np.uint8)
    # 下阈值
    lower_hsv = np.array([0, 0, 0])
    # 上阈值
    # hue:0~180 saturation:0~255, value:0~255
    upper_hsv = np.array([180, 255, 255])
    # hsv 变化比率
    hsv_rate = np.array([upper_hue, upper_saturation, upper_value])
    # mask = cv.inRange(hsv_img, lower_hsv, upper_hsv, mask)

    for r in range(hsv_img.shape[0]):
        max_pixel = np.max(hsv_img[r], axis=0)
        min_pixel = np.min(hsv_img[r], axis=1)
        for k in range(hsv_img.shape[2]):
            # if mask[r, c] == 255:
            #     dst_hsv_img[r, c] = hsv_img[r, c]
            # else:
            #     for k in range(3):
            #         dst_hsv_img[r][c][k] = int(upper_hsv[k])*(int(hsv_img[r][c][k])-int(min_pixel[k]))\
            #                                / (int(max_pixel[k]) - int(min_pixel[k]))
            dst_hsv_img[r][:, k] = hsv_img[r][:, k] * hsv_rate[k]
            print(dst_hsv_img)
            for c in range(hsv_img.shape[1]):
                if dst_hsv_img[r][c][k] > max_pixel[k]:
                    dst_hsv_img[r][c][k] = hsv_img[r][c][k]

    dst_img = cv.cvtColor(np.uint8(dst_hsv_img), cv.COLOR_HSV2BGR)
    return dst_img


if __name__ == "__main__":
    random_index = random.sample((np.arange(3).tolist()), 2)

    path = os.path.abspath('..\\..\\..') + '\\databases\\image'
    img_path = os.path.join(path, 'girl.jpg')
    src_img = cv.imread(img_path)

    dst_hsv_img = hsv_adjustment(src_img, 1, 0.9, 1)

    cv.imshow('src image', src_img)
    cv.imshow('dst hsv image', dst_hsv_img)

    cv.waitKey(0)







# !_*_ coding:utf8 _*_
# @function PIL 修改图像分辨率
# @Author alexchung
# @Date 23/8/2019 11:26 AM

import os
import cv2 as cv
from PIL import Image as im

if __name__ == "__main__":

    path = os.path.abspath('..\\..\\..') + '\\databases\\image'

    img_path = os.path.join(path, 'girl.jpg')
    new_img_path = os.path.join(path, 'dpi_girl.jpg')

    src_img = cv.imread(img_path)
    PIL_image = im.open(new_img_path)

    img_dpi = PIL_image.info['dpi']
    image = im.fromarray(cv.cvtColor(src_img, cv.COLOR_BGR2RGB))

    PIL_image.show()
    PIL_image.save(new_img_path, dpi=(img_dpi[0]/2, img_dpi[1]/2,))

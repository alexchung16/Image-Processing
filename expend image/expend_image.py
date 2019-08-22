# !_*_ coding:utf8 _*_
# @function 图像扩增
# @Author alexchung
# @Date 19/8/2019 14:56 PM

import os 
import cv2 as cv
import numpy as np
import random


class MultipleProcessingImage(object):
    def __init__(self, src_path, dst_path, expend_rate=10, processing_depth=2, category_name=''):
        """
        构造函数
        :param src_path:
        :param dst_path:
        :param expend_rate:
        :param processing_depth:
        :param category_name:
        """
        self.src_path = src_path
        self.dst_path = dst_path
        self.expend_rate = expend_rate
        self.processing_depth = processing_depth
        self.category_name = category_name
        self.image_index = 0
        self.process_method = {
                                1: 'sizeImage',
                                2: 'rotationImage',
                                3: 'perspectiveTransformImage',
                                4: 'noiseImage',
                                5: 'blurImage',
                                6: 'lightImage',
                                7: 'contrastImage',
                                8: 'sharpingImage',
                                9: 'hueImage',
                                10: 'saturationImage'
                             }

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

    def run(self):
        """
        运行程序
        :return:
        """
        self.readProcessingSaveImage()
        print('This time successfully process of ' + str(self.image_index) + 'figures')

    def getProcessingMethod(self):
        """
        获取方法列表
        :return:
        """

        return self.process_method.values()

    @classmethod
    def setProcessMethod(self, method):

        self.process_method = method

    def sizeImage(self, img):
        """
        修改图片尺寸
        :param img:
        :return:
        """
        size_img = np.array
        random_index = np.random.randint(0, 2, 1)[0]
        if random_index == 0:
            # 扩大图片(enlarge image)
            size_img = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
        elif random_index == 1:
            # 缩小图片(shrink image)
            size_img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
        return size_img

    def rotationImage(self, img):
        """
        旋转图片
        :param img:
        :return:
        """
        h, w = img.shape[:2]
        rotation_angles = [45, 90, 180]
        # getRotationMatrix2D(center, angle, scale)
        # center 中心
        # angle 角度
        # scale 尺度
        # 生成随机索引
        random_index = np.random.randint(0, len(rotation_angles))
        angle = rotation_angles[random_index]
        r = cv.getRotationMatrix2D((w / 2.0, h / 2.0), angle, 1)
        rotation_img = cv.warpAffine(img, r, (w, h), borderValue=[0, 0, 0])

        return rotation_img

    def perspectiveTransformImage(self, img):
        """
        透视变换
        :param img:
        :return:
        """
        h, w = img.shape[:2]
        respective_img = np.array

        # 透视变换
        src0 = np.array([[0, 0], [0, w - 1], [h - 1, 0], [w - 1, h - 1]], np.float32)
        dst0 = np.array([[0, h * 0.4], [0, w - 1], [h - 1, 0], [w - 1, h * 0.6]], np.float32)
        # 计算投影变换的矩阵
        p0 = cv.getPerspectiveTransform(src0, dst0)
        # 利用计算出的矩阵对图片做投影
        src1 = np.array([[0, 0], [0, w - 1], [h - 1, 0], [w - 1, h - 1]], np.float32)
        dst1 = np.array([[0, 0], [w * 0.6, 0], [w * 0.4, h - 1], [w - 1, h - 1]], np.float32)
        p1 = cv.getPerspectiveTransform(src1, dst1)

        random_index = np.random.randint(0, 2)
        if random_index == 0:
            respective_img = cv.warpPerspective(img, p0, (w, h), borderValue=[0, 0, 0])
        elif random_index == 1:
            respective_img = cv.warpPerspective(img, p1, (w, h), borderValue=[0, 0, 0])

        return respective_img

        # 噪声(noise)

    def GaussianNoise(self, image, mean=0, var=0.001):
        """
        高斯噪声
        :param image: 源图片
        :param mean: 均值
        :param var: 方差
        :return:
       """
        image = np.array(image / 255, dtype=float)
        noise = np.random.normal(mean, var ** 0.5, image.shape)
        dst_img = image + noise
        if dst_img.min() < 0:
            low_clip = -1.
        else:
            low_clip = 0.
        dst_img = np.clip(dst_img, low_clip, 1.0)
        dst_img = np.uint8(dst_img * 255)
        return dst_img

    def SPNoise(self, image, prob=0.005):
        """
        椒盐噪声
        :param image: 源图片
        :param prob: 噪声比例
        :return:
        """
        dst_img = np.zeros(image.shape, np.uint8)
        thres = 1 - prob
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rdn = random.random()
                if rdn < prob:
                    dst_img[i][j] = 0
                elif rdn > thres:
                    dst_img[i][j] = 255
                else:
                    dst_img[i][j] = image[i][j]
        return dst_img

    def noiseImage(self, img):
        """
        噪声图片
        :param img:
        :return:
        """
        noise_img = np.array
        random_index = np.random.randint(0, 2)
        if random_index == 0:
            noise_img = self.GaussianNoise(img)
        elif random_index == 1:
            noise_img = self.SPNoise(img)

        return noise_img

    def blurImage(self, img):
        """
        模糊(滤波filter)
        :param img:
        :return:
        """
        blur_img = np.array
        random_index = np.random.randint(0, 3)

        if random_index == 0:
            # 均值滤波
            blur_img = cv.blur(img, (5, 5))
        elif random_index == 1:
            # 高斯滤波
            blur_img = cv.GaussianBlur(img, (5, 5), 0)
        elif random_index == 2:
            # 双边滤波
            blur_img = cv.bilateralFilter(img, 9, 75, 75)

        return blur_img

    def lightImage(self, img):
        """
        亮度变换
        :param img:
        :return:
        """
        light_img = np.array
        random_index = np.random.randint(0, 2)
        # 亮度变换 g(x) = αf(x) + β
        if random_index == 0:
            # 提高亮度
            light_img = np.uint8(np.clip((1.0 * img + 20), 0, 255))
        elif random_index == 1:
            # 降低亮度
            light_img = np.uint8(np.clip((1.0 * img - 20), 0, 255))
        return light_img

    def contrastImage(self, img):
        """
        对比度变化
        :param img:
        :return:
        """
        contrast_img = np.array
        random_index = np.random.randint(0, 2)
        # 亮度变换 g(x) = αf(x) + β
        if random_index == 0:
            # 提高亮度
            contrast_img = np.uint8(np.clip((1.0 * img + 20), 0, 255))
        elif random_index == 1:
            # 降低亮度
            contrast_img = np.uint8(np.clip((1.0 * img - 20), 0, 255))
        return contrast_img

    def sharpingImage(self, img):
        """
        锐度调整
        :param img: 源图像
        :return:
        """
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
        dst_img = cv.filter2D(img, -1, kernel=kernel)
        return dst_img

    def hsvImage(self, img, hue_rate, saturation_rate, value_rate):
        """
        色调 饱和度调整
        :param img: 原图像
        :param hue_rate: 色相调整比率
        :param saturation_rate: 饱和度调整比率
        :param value_rate: 明度调整比率
        :return:
        """
        hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        dst_hsv_img = np.zeros(hsv_img.shape, dtype=np.uint8)

        hsv_upper = np.array([180, 255, 255])
        # hsv 变化比率
        hsv_rate = np.array([hue_rate, saturation_rate, value_rate])
        # mask = cv.inRange(hsv_img, lower_hsv, upper_hsv, mask)
        #
        for r in range(hsv_img.shape[0]):
            max_pixel = np.max(hsv_img[r], axis=0)
            min_pixel = np.min(hsv_img[r], axis=1)
            for k in range(hsv_img.shape[2]):
                dst_hsv_img[r][:, k] = hsv_img[r][:, k] * hsv_rate[k]
                for c in range(hsv_img.shape[1]):
                    if dst_hsv_img[r][c][k] == hsv_upper[k]:
                        dst_hsv_img[r][c][k] = hsv_img[r][c][k]

        dst_img = cv.cvtColor(np.uint8(dst_hsv_img), cv.COLOR_HSV2BGR)
        return dst_img
    # def multipleProcessImage(img=np.array, expend_rate=10, processing_depth=2, save_path='', category_name=''):
    def multipleProcessImage(self, img=np.array):
        """
        图片多重处理
        :param img: 源图片
        :param expend_rate: 扩张倍数
        :param processing_depth: 处理深度
        :param save_path: 保存路径
        :param category_name: 分类名称
        :return:
        """
        # 检查保存路径
        for i in range(self.expend_rate):
            process_img = img
            depth = np.random_index = np.random.randint(1, self.processing_depth + 1)
            process_index = sorted(random.sample((np.arange(1, len(self.process_method) + 1).tolist()), depth))
            for index in process_index:
                if self.process_method[index] == 'sizeImage':
                    process_img = self.sizeImage(process_img)
                elif self.process_method[index] == 'rotationImage':
                    process_img = self.rotationImage(process_img)
                elif self.process_method[index] == 'perspectiveTransformImage':
                    process_img = self.perspectiveTransformImage(process_img)
                elif self.process_method[index] == 'noiseImage':
                    process_img = self.noiseImage(process_img)
                elif self.process_method[index] == 'blurImage':
                    process_img = self.blurImage(process_img)
                elif self.process_method[index] == 'lightImage':
                    process_img = self.lightImage(process_img)
                elif self.process_method[index] == 'contrastImage':
                    process_img = self.contrastImage(process_img)
                elif self.process_method[index] == 'sharpingImage':
                    process_img = self.sharpingImage(process_img)
                elif self.process_method[index] == 'hueImage':
                    process_img = self.hsvImage(process_img, 0.8, 1, 1)
                elif self.process_method[index] == 'saturationImage':
                    process_img = self.hsvImage(process_img, 1, 0.8, 1)

            img_path = os.path.join(self.dst_path, self.category_name + '_' + str(self.image_index) + '.jpg')
            cv.imwrite(img_path, process_img)
            self.image_index += 1

    def readProcessingSaveImage(self):
        """
        读取 处理 保存图片
        :return:
        """
        if self.mkdirCheck(self.src_path) is False:
            exit(self.src_path + ' is not exit please check it')

        self.mkdirCheck(self.dst_path, True)
        # 获取目录下图片列表
        img_list = os.listdir(self.src_path)

        for img_name in img_list:
            try:
                img_path = os.path.join(self.src_path, img_name)
                img = cv.imread(img_path)
                self.multipleProcessImage(img)
                print(img_name + ' has been successfully expended')
            except Exception as e:
                print(img_name + ' encountered a mistake, please check it later on')
                continue
            finally:
                print('current processing image is'+img_name)


if __name__ == "__main__":

    path = os.path.abspath('..\\..\\..') + '\\databases\\fruit_vegetables\\tomatoes'
    new_path = os.path.abspath('..\\..\\..') + '\\databases\\fruit_vegetables\\new_tomatoes'

    process = MultipleProcessingImage(src_path=path, dst_path=new_path, category_name='tomatoes')
    process.run()
    # print(process.process_method)


    # cv.imshow('image', img)
    # cv.imshow('expend', sizeImage(img))
    # cv.imshow('rotation', rotationImage(img))
    #
    # cv.imshow('respective', perspectiveTransformImage(img))
    # #
    # cv.imshow('noise', noiseImage(img))
    #
    # cv.imshow('blur', blurImage(img))
    # cv.imshow('light', lightImage(img))
    # cv.imshow('contrast', contrastImage(img))
    # cv.waitKey(0)


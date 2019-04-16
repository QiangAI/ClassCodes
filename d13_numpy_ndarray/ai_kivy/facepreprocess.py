# coding=utf-8
import os
import random

import cv2
import numpy as np


# 统一尺寸
# 增加灰度


class FacePreprocess:
    input_dir = None
    output_dir = None

    def __init__(self, i_dir, o_dir):
        self.input_dir = i_dir
        self.output_dir = o_dir

    def preprocess(self):
        # 得到训练的图像类别目录
        paths = os.listdir(self.input_dir)
        # 循环处理每个类别目录下的图像（调用一个函数处理每个目录）
        for path_item in paths:
            self.handle_images(path_item)

    def handle_images(self, path_item):
        out_path_item = os.path.join(self.output_dir, path_item)
        if not os.path.exists(out_path_item):
            os.makedirs(out_path_item)
        in_path_item = os.path.join(self.input_dir, path_item)
        files = os.listdir(in_path_item)
        for file in files:
            img = cv2.imread(os.path.join(in_path_item, file))
            img = cv2.resize(img, dsize=(32, 32))
            for i in range(3):
                img = self.img_gray(img, random.uniform(0.8, 1.2), random.randint(-30, 30))
                dst_path = os.path.join(
                    out_path_item,
                    '%s_%d%s' % (os.path.splitext(file)[0], i + 1, os.path.splitext(file)[1]))
                cv2.imwrite(dst_path, img)

    @staticmethod
    def img_gray(img, alpha=1, bias=0):
        # 改变图像灰度，这样训练的图像，在识别不受光线影响
        img = img.astype(float)
        img = img * alpha + bias
        img[img < 0] = 0
        img[img > 255] = 255
        img = img.astype(np.uint8)
        return img

    def read_image(self):
        data_ = []
        target_ = []
        target_dict_ = {}
        paths = os.listdir(self.output_dir)
        index = 0
        # 循环处理每个类别目录下的图像（调用一个函数处理每个目录）
        for path_item in paths:
            target_dict_[index] = path_item
            out_path_item = os.path.join(self.output_dir, path_item)
            files = os.listdir(out_path_item)
            for file in files:
                img = cv2.imread(os.path.join(out_path_item, file))
                data_.append(img)
                target_.append(index)
            index += 1
        return np.array(data_), np.array(target_), target_dict_

    def get_target_dict(self):
        target_dict_ = {}
        paths = os.listdir(self.output_dir)
        index = 0
        for path_item in paths:
            target_dict_[index] = path_item
            index += 1
        return target_dict_
# pp = FacePreprocess('images/', 'trains/')
# pp.preprocess()
# data, target, target_dict = pp.read_image()
# print(data.shape, target.shape, target_dict)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ File file_compress.py
# @ Description :
# @ Author alexchung
# @ Time 2/12/2019 PM 16:14

import os
import zipfile
import tarfile
import time

zip_file = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test/test1575272889.zip'
dst_dir = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test'



def show_info(zip_file):
    """
    show zip file info
    :param zip_file:
    :return:
    """
    with zipfile.ZipFile(zip_file) as zip:
        for info in zip.infolist():
            print(info.filename + ':',
                  'compress_size ' + str(info.compress_size) + ' bytes',
                  'file_size ' + str(info.file_size) + ' bytes')
        for name in zip.namelist():
            print(name)
        zip.printdir()


def file_extract(zip_file_path, dst_path):
    """
    extract file from a zip file
    :param zip_path:
    :param dst_path:
    :return:
    """
    with zipfile.ZipFile(zip_file_path, mode='r') as zip:
        zip.extractall(path=dst_path)
        print('All file unzip to '+dst_path)


if __name__ == "__main__":
    file_extract(zip_file, dst_dir)
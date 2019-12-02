#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ File file_compress.py
# @ Description :
# @ Author alexchung
# @ Time 2/12/2019 PM 16:14

import os
import zipfile
import tarfile
import rarfile
import time

zip_file = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test/test1575272889.zip'
tar_file = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test/test1575277216.tar.gz'
rar_file = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test/test.rar'
dst_dir = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test'

def show_info_zip(zip_file):
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


def file_unpack_zip(zip_file_path, dst_path):
    """
    extract file from a zip file
    :param zip_path:
    :param dst_path:
    :return:
    """
    try:
        with zipfile.ZipFile(zip_file_path, mode='r') as zip:
            zip.extractall(path=dst_path)
            print('All file unzip to '+dst_path)
        return True
    except Exception as e:
        print(e)
        return False


def file_unpack_tar(tar_file_path, dst_path):
    """
    extract file from a tar file
    :param tar_file_path:
    :param dst_path:
    :return:
    """
    try:
        with tarfile.open(tar_file_path, mode='r:gz') as tar:
            tar.extractall(path=dst_path)
            print('All file unpack to '+dst_path)
            return True
    except Exception as e:
        print(e)
        return False


def file_unpack_rar(rar_file_path, dst_path):
    """
    extract file from a rar file
    :param rar_file_path:
    :param dst_path:
    :return:
    """
    # error => Unrar not installed? (rarfile.UNRAR_TOOL='unrar') ubuntu
    # solve => sudo apt-get install rar unrar
    try:
        with rarfile.RarFile(rarfile=rar_file_path, mode='r') as rar:
            rar.extractall(path=dst_path)
            print('All file unpack to '+dst_path)
            return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    # file_unpack_zip(zip_file, dst_dir)

    file_unpack_rar(rar_file, dst_dir)
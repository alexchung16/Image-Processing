#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ File file_compress.py
# @ Description :
# @ Author alexchung
# @ Time 2/12/2019 AM 11:31

import os
import zipfile
import tarfile
import time


src_dir = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test'
dst_dir = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test'


def file_generator(file_dir):
    """
    get all file path from file_dir
    :param file_dir:
    :return:
    """
    files_path = []
    arc_path = []
    # current_dir = str()
    parent_dir = os.path.split(file_dir)[0]
    for root, directories, files in os.walk(file_dir):
        # current_dir = os.path.join(current_dir, os.path.split(root)[-1])
        for file in files:
            file_path = os.path.join(root, file)
            files_path.append(file_path)
            arc_path.append(file_path.replace(parent_dir, ''))
    return files_path, arc_path

    # print(file_generator(src_dir))


def file_compress_zip(src_dir, dst_dir):
    """
    writing file to a zip file
    :param src_dir:
    :param dst_dir:
    :return:
    """
    # get time stamp to generate zip filename
    time_stamp = time.time()
    zip_file_path = os.path.join(dst_dir, os.path.split(src_dir)[-1] + str(int(time_stamp)) + '.zip')
    try:
        file_path, arc_path = file_generator(src_dir)
        with zipfile.ZipFile(file=zip_file_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
            for file, arc_file in zip(file_path, arc_path):
                zip_file.write(filename=file, arcname=arc_file)
        print('All file zipped successfully')
        return True
    except Exception as e:
        print(e)
        return False

def file_compress_tar(src_dir, dst_dir):
    """
    writing file to a tar file
    :param src_dir:
    :param dst_dir:
    :return:
    """
    # get time stamp to generate zip filename
    time_stamp = time.time()

    tar_file_path = os.path.join(dst_dir, os.path.split(src_dir)[-1] + str(int(time_stamp)) + '.tar.gz')
    arc_dir = os.path.basename(src_dir)
    try:
        with tarfile.open(tar_file_path, mode='w:gz') as tar_file:
            tar_file.add(name=src_dir, arcname=arc_dir)
        print('All file compress successfully')
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":

    # # get zip filename
    # if src_dir.split('/')[-1] == '/':
    #     zip_file_path = os.path.join(dst_dir, src_dir.split('/')[-2] + str(int(time_stamp)) + '.zip')
    # else:
    #     zip_file_path = os.path.join(dst_dir, src_dir.split('/')[-1] + str(int(time_stamp)) + '.zip')
    # zip_file_path = os.path.join(dst_dir, os.path.split(src_dir)[-1]+ str(int(time_stamp)) + '.zip')
    # file_compress_zip(src_dir, dst_dir)
    # file_compress_tar(src_dir, dst_dir)

    print(os.path.isdir(src_dir))

    if src_dir.endswith('/'):
        src_dir = src_dir[:-1]













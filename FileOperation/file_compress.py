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
zip_file = '/home/alex/Documents/datasets/dogs_vs_cat_separate/test/test1575268415.zip'


if __name__ == "__main__":
    time_stamp = time.time()

    # # get zip filename
    # if src_dir.split('/')[-1] == '/':
    #     zip_file_path = os.path.join(dst_dir, src_dir.split('/')[-2] + str(int(time_stamp)) + '.zip')
    # else:
    #     zip_file_path = os.path.join(dst_dir, src_dir.split('/')[-1] + str(int(time_stamp)) + '.zip')
    zip_file_path = os.path.join(dst_dir, os.path.split(src_dir)[-1]+ str(int(time_stamp)) + '.zip')




    def file_generator(file_dir):
        """
        get all file path from file_dir
        :param file_dir:
        :return:
        """
        files_path = []
        arc_path = []
        # current_dir = str()
        parent_dir = os.path.split(src_dir)[0]
        for root, directories, files in os.walk(src_dir):
            # current_dir = os.path.join(current_dir, os.path.split(root)[-1])
            for file in files:
                file_path = os.path.join(root, file)
                files_path.append(file_path)
                arc_path.append(file_path.replace(parent_dir, ''))
        return files_path, arc_path

    # print(file_generator(src_dir))

    def file_compress(src_dir, dst_dir):
        """
        writing file to a zipfile
        :param src_dir:
        :param dst_dir:
        :return:
        """
        # get time stamp to generate zip filename
        time_stamp = time.time()

        zip_file_path = os.path.join(dst_dir, os.path.split(src_dir)[-1] + str(int(time_stamp)) + '.zip')

        file_path, arc_path = file_generator(src_dir)

        with zipfile.ZipFile(file=zip_file_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
            for file, arc_file in zip(file_path, arc_path):
                zip_file.write(filename=file, arcname=arc_file)
        print('All file zipped successfully')

    file_compress(src_dir, dst_dir)

    def file_extract(zip_path):
        pass




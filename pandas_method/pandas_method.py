#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : pandas_method.py
# @Author  : MoonKuma
# @Date    : 2019/3/15
# @Desc   : some related methods

import os
import pandas as pd

def get_file_list(file_path, start, end):
    """
    get the file dict of same patten
    :param file_path: file path
    :param start: patten starts with, like 'sub'
    :param end: patten ends with, like 'ave-fif' or 'tfr-h5'
    :return: dict object {'sub3':os.path.abspath(sub3)}
    """
    file_dict = dict()  # {'sub3':'data/sample_data/sample_result/pain_ave/sub5-ave.fif'}
    files = os.listdir(file_path)
    for file_name in files:
        if file_name.startswith(start) and file_name.endswith(end):
            inner_file = os.path.join(file_path, file_name)
            key = file_name.replace(end, '')
            file_dict[key] = os.path.abspath(inner_file)
    return file_dict
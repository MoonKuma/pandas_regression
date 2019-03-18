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


def pick_columns(columns, word_starts_with=None, word_ends_with=None):
    """
    Pick columns with comparing starts and ends
    :param columns: list [iterable object] of full columns
    :param word_starts_with:  to start with certain string
    :param word_ends_with:  to end with certain string
    :return: the selected list
    """
    col_picked_start = list()
    col_picked_end = list()
    col_picked_both = list()
    for word in columns:
        if word_starts_with is not None and str(word).startswith(word_starts_with):
            col_picked_start.append(word)
        if word_ends_with is not None and str(word).endswith(word_ends_with):
            col_picked_end.append(word)
        if word_starts_with is not None and str(word).startswith(word_starts_with) and word_ends_with is not None and str(word).endswith(word_ends_with):
            col_picked_both.append(word)
    if word_starts_with is not None and word_ends_with is None:
        return col_picked_start
    if word_starts_with is None and word_ends_with is not None:
        return col_picked_end
    if word_starts_with is not None and word_ends_with is not None:
        return col_picked_both



#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : test_hypothesis.py
# @Author  : MoonKuma
# @Date    : 2019/3/19
# @Desc   :  test hypothesis

from sklearn_method.prepare_hypothesis import prepare_hypothesis

file_name = 'data/data_formal/orig/txt_file/merged_data/result_final.txt'

df, columns_dict_x, columns_dict_y = prepare_hypothesis(file_name=file_name)

# test one model and all hypothesis

# test one hypothesis and all models

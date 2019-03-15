#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : read_questionnaire.py
# @Author  : MoonKuma
# @Date    : 2019/3/15
# @Desc   :  Designed to read questionnaire from chongqing's data

import os
import re
import pandas as pd
from pandas_method import pandas_method

file_path = 'data/data_formal/orig/txt_file'
file_dict = pandas_method.get_file_list(file_path=file_path, start='chongqing_', end='.txt')

full_data = None
for file_head in file_dict.keys():
    file_name = file_dict[file_head]
    df = pd.read_csv(file_name, delimiter='\t', header=0, index_col=0)
    if full_data is None:
        full_data = df
    else:
        full_data = pd.concat([full_data, df])

patten = r'r[0-9]'
index = full_data.index.values
columns = full_data.columns.values
columns_stay = list()
for col_name in columns:
    str_col = str(col_name)
    if str_col.startswith('age_') or str_col.startswith('sex_') or re.match(patten,str_col):
        columns_stay.append(str_col)
df_picked = pd.DataFrame(full_data, columns=columns_stay, index=index)

# save total result
save_file = 'data/data_formal/orig/txt_file/merged_data/total_saved.txt'
df_picked.to_csv(save_file)

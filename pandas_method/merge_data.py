#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : merge_data.py
# @Author  : MoonKuma
# @Date    : 2019/3/17
# @Desc   : merging them

import pandas as pd

file_1 = 'data/data_formal/orig/erp/pain_eeg_result_v19.txt'
df1 = pd.read_csv(file_1, delimiter=',', header=0, index_col=0)
df1 = df1[~df1.index.duplicated(keep='first')]

file_2 = 'data/data_formal/orig/erp/pain_erp_result_v8849.txt'
df2 = pd.read_csv(file_2, delimiter=',', header=0, index_col=0)
df2 = df2[~df2.index.duplicated(keep='first')]

file_3 = 'data/data_formal/orig/erp/rest_eeg_result_v7336.txt'
df3 = pd.read_csv(file_3, delimiter=',', header=0, index_col=0)
df3 = df3[~df3.index.duplicated(keep='first')]

file_4 = 'data/data_formal/orig/txt_file/merged_data/total_computed.txt'
df4 = pd.read_csv(file_4, delimiter=',', header=0, index_col=0)
df4['index_new'] = df4.index.map(lambda x: int(str(x).replace('\'','').replace('nan','0')))
df4 = df4.set_index(keys='index_new')

result = df4.join(df1,how='inner')
result = result.join(df2,how='inner')
result = result.join(df3,how='inner')

save_file = 'data/data_formal/orig/txt_file/merged_data/result_final.txt'
result.to_csv(save_file)
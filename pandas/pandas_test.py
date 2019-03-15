#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pandas_test.py
# @Author: MoonKuma
# @Date  : 2019/3/12
# @Desc  : test function in pandas

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

file_name = 'data/data_formal/env_zoneid_data.txt'

# read
full_data = pd.read_csv(file_name, delimiter='\t', header=0)  # no index here, index_col=0 if index required

# split infoy
full_data['project'] = full_data['eov'].map(lambda x: x.split('_')[0].replace('2',''))
full_data['local'] = full_data['eov'].map(lambda x: x.split('_')[1])

# one hot
dummy_col = ['project', 'local']
full_data = pd.get_dummies(full_data, columns=dummy_col)

# normalize by column (use StandardScaler to get a normal distribution with 0 mean and 1 std-error, this also accept NA)
# you need the latest scikit-learn packages, try : conda update scikit-learn
scaler = StandardScaler()
norm_col = ['money', 'user', 'new_pay', 'new_pay', 'reten29']
index = full_data.index.values
columns = full_data.columns.values
column_stay = list()
for key in list(columns):
    if key not in norm_col:
        column_stay.append(key)
norm_data = pd.DataFrame(full_data, columns=norm_col).values
norm_ndarray = scaler.fit(norm_data).transform(norm_data)
norm_df = pd.DataFrame(norm_ndarray, columns=norm_col, index=index)
merge_df = pd.merge(norm_df, pd.DataFrame(full_data, columns=column_stay), left_index=True, right_index=True)




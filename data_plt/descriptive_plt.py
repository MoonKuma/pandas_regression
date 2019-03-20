#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : descriptive_plt.py
# @Author: MoonKuma
# @Date  : 2019/3/18
# @Desc  : plot descriptive plot

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_method.pandas_method import pick_columns
from data_plt.plt_method import box_plot_selected

# read in
file_name = 'data/data_formal/orig/txt_file/merged_data/result_final.txt'
df = pd.read_csv(filepath_or_buffer=file_name, sep=',', header=0, index_col=0)

# get columns
columns = df.columns.values
col = columns.reshape(columns.shape[0],1)

# rest
# rest_eeg_orig
# rest_eeg_norm
starts = 'rest_norm'
sub_col_rest = pick_columns(columns=columns, word_starts_with=starts)

# pain
# pain norm

starts = 'pain_erp_peak'
ends = 'N90'
fig = box_plot_selected(df=df, starts=starts,ends=ends)

starts = 'pain_eeg_norm'
ends = '_F_T0_F_10.0'
fig = box_plot_selected(df=df, starts=starts,ends=ends)


def plot_starts_ends(df, starts, ends, if_save=True):
    fig = box_plot_selected(df=df, starts=starts,ends=ends)
    file_save_path = 'data/data_formal/'
    file_save_name = file_save_path + starts + '_' + ends + '.jpg'
    if if_save:
        fig.savefig(file_save_name)

plot_starts_ends(df, starts='pain_eeg_norm', ends='_F_T0_C_10.0', if_save=True)
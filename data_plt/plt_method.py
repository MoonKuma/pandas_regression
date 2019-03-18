#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : plt_method.py
# @Author: MoonKuma
# @Date  : 2019/3/18
# @Desc  :

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_method.pandas_method import pick_columns


def box_plot_selected(df, starts, ends):
    columns = df.columns.values
    sub_col_pain_peak = pick_columns(columns=columns, word_starts_with=starts, word_ends_with=ends)
    # box plot on certain cols
    df_index = df.index.values
    sub_df = pd.DataFrame(df, columns=sub_col_pain_peak, index=df_index)
    label_list = list()
    for i in sub_col_pain_peak:
        label_list.append(i.replace(starts, '').replace(ends, ''))
    title = starts + '(' + ends + ')'
    data_list = list()
    for col in sub_col_pain_peak:
        data_list.append(sub_df[col])
    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.boxplot(data_list, labels=label_list)
    fig = plt.gcf()
    plt.show()
    return fig

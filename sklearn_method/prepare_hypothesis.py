#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : test_hypothesis.py
# @Author  : MoonKuma
# @Date    : 2019/3/18
# @Desc   : test hypothesis in chongqing

import pandas as pd
from pandas_method.pandas_method import pick_columns
from sklearn.datasets import make_regression

def prepare_hypothesis(file_name):
    """
    Prepare data frame, feature columns and target columns for future test
    This method also create a faked feature and target sets for testing whether the model worked
    :param file_name: file where data saved
    :return: df, columns_dict_x, columns_dict_y
    """
    # data
    # file_name = 'data/data_formal/orig/txt_file/merged_data/result_final.txt'
    df = pd.read_csv(filepath_or_buffer=file_name, sep=',', header=0, index_col=0)
    # columns = df.columns.values
    # col_T = columns.reshape(columns.shape[0],1) # this is for easier reading
    indexs = df.index.values
    # fake data
    X, y = make_regression(n_features=50, n_samples=df.shape[0], n_informative=25, bias=0.1, noise=0.2)
    X_col = list()
    for i in range(0,X.shape[1]):
        col_name = 'test_X_' + str(i)
        X_col.append(col_name)
    Y_col = ['test_Y']
    df_testx = pd.DataFrame(X, columns=X_col, index=indexs)
    df_testy = pd.DataFrame(y.reshape(y.shape[0],1), columns=Y_col,index=indexs)
    df = df.join(df_testx)
    df = df.join(df_testy)
    columns = df.columns.values
    # columns
    columns_dict_y = dict()
    """
    The following is all hypothesises,  columns_dict_y contains targets, and columns_dict_x contains features combination
    """
    # target
    columns_dict_y['age'] = pick_columns(columns=columns, word_starts_with='age_response')
    columns_dict_y['race_identity'] = pick_columns(columns=columns, word_starts_with='RESULT_r1')
    columns_dict_y['face_recognition'] = pick_columns(columns=columns, word_starts_with='RESULT_r2')
    columns_dict_y['day_dream'] = pick_columns(columns=columns, word_starts_with='RESULT_r3')
    columns_dict_y['IRI_FS'] = pick_columns(columns=columns, word_starts_with='RESULT_r4_FS')
    columns_dict_y['IRI_EC'] = pick_columns(columns=columns, word_starts_with='RESULT_r4_EC')
    columns_dict_y['IRI_PT'] = pick_columns(columns=columns, word_starts_with='RESULT_r4_PT')
    columns_dict_y['IRI_PD'] = pick_columns(columns=columns, word_starts_with='RESULT_r4_PD')
    columns_dict_y['Interdependent'] = pick_columns(columns=columns, word_starts_with='RESULT_r5_Interdependent')
    columns_dict_y['Independent'] = pick_columns(columns=columns, word_starts_with='RESULT_r5_Independent')
    columns_dict_y['altruism'] = pick_columns(columns=columns, word_starts_with='RESULT_r6_')
    columns_dict_y['anxiety'] = pick_columns(columns=columns, word_starts_with='RESULT_r7_')
    columns_dict_y['depression'] = pick_columns(columns=columns, word_starts_with='RESULT_r8_')
    # test target (for testing whether the method is useful)
    columns_dict_y['test_Y'] = pick_columns(columns=columns, word_starts_with='test_Y')

    # features
    columns_dict_x = dict()
    # pain
    # pain eeg
    columns_dict_x['pain_eeg_norm'] = pick_columns(columns=columns, word_starts_with='pain_eeg_norm_')
    columns_dict_x['pain_eeg_norm_Pain_'] = pick_columns(columns=columns, word_starts_with='pain_eeg_norm_Pain_')
    columns_dict_x['pain_eeg_norm_Neutral_'] = pick_columns(columns=columns, word_starts_with='pain_eeg_norm_Neutral_')
    columns_dict_x['pain_eeg_orig'] = pick_columns(columns=columns, word_starts_with='pain_eeg_orig_')
    columns_dict_x['pain_eeg_orig_Pain_'] = pick_columns(columns=columns, word_starts_with='pain_eeg_orig_Pain_')
    columns_dict_x['pain_eeg_orig_Neutral_'] = pick_columns(columns=columns, word_starts_with='pain_eeg_orig_Neutral_')
    # pain erp
    # amplitude
    columns_dict_x['pain_erp_amplitude_norm'] = pick_columns(columns=columns, word_starts_with='pain_erp_amplitude_norm_')
    columns_dict_x['pain_erp_amplitude_norm_Pain_'] = pick_columns(columns=columns, word_starts_with='pain_erp_amplitude_norm_Pain_')
    columns_dict_x['pain_erp_amplitude_norm_Neutral_'] = pick_columns(columns=columns, word_starts_with='pain_erp_amplitude_norm_Neutral_')
    columns_dict_x['pain_erp_amplitude_orig'] = pick_columns(columns=columns, word_starts_with='pain_erp_amplitude_orig_')
    columns_dict_x['pain_erp_amplitude_orig_Pain_'] = pick_columns(columns=columns, word_starts_with='pain_erp_amplitude_orig_Pain_')
    columns_dict_x['pain_erp_amplitude_orig_Neutral_'] = pick_columns(columns=columns, word_starts_with='pain_erp_amplitude_orig_Neutral_')
    # peak
    columns_dict_x['pain_erp_peak'] = pick_columns(columns=columns, word_starts_with='pain_erp_peak_')
    # rest
    columns_dict_x['rest_norm'] = pick_columns(columns=columns, word_starts_with='rest_norm_')
    columns_dict_x['rest_orig'] = pick_columns(columns=columns, word_starts_with='rest_orig_')
    # testing features (for testing whether the method is useful)
    columns_dict_x['test_X'] = pick_columns(columns=columns, word_starts_with='test_X_')

    return df, columns_dict_x, columns_dict_y
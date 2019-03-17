#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : compute_questionnaire.py
# @Author  : MoonKuma
# @Date    : 2019/3/17
# @Desc   : compute result of questionnaire

import pandas as pd
import numpy as np

def clean_list(list_to_clean, refer_list):
    result_list = list()
    for i in list_to_clean:
        if i not in  refer_list :
            result_list.append(i)
    return result_list

# score_dict_total
score_dict_total = {'r1_':{0:[13,14,15],
                           1:list(range(1,13))},
                    'r2_':{0:[8,10,15,16,23],
                           1:clean_list(list(range(1,24)), refer_list=[8,10,15,16,23,2,3,4,6,9,13,19,20]),
                           -1:[2,3,4,6,9,13,19,20]},
                    'r3_':{1:list(range(1,25))}
                    }

# get data
def get_sliced_data(full_data, col_head):
    columns = full_data.columns.values
    index = full_data.index.values
    column_remain = list()
    for i in columns:
        if str(i).startswith(col_head):
            column_remain.append(i)
    return pd.DataFrame(full_data, columns=column_remain, index=index)

# missing type
def missing_type1(value):
    if value<0 or value>256 or type(value)==str:
        return True

# rm missing value
def rm_missing_value(df, missing_type, fix_value):
    columns = df.columns.values
    index = df.index.values
    # lambda
    def do_lambda(x):
        if missing_type(x):
            return fix_value
        else:
            return x
    for column in columns:
        df[column] = df[column].map(lambda x: do_lambda(x))
    df.fillna(fix_value)

# get question index
def get_question(question_head):
    return int(question_head.split('_')[1])

# transform score dict
def form_score(score_dict):
    new = dict()
    for key in score_dict.keys():
        question_list = score_dict[key]
        for value in question_list:
            new[value] = key
    return new


def compute_questionnaire(df, questionnaire_name, question_score_name):
    # selected_data = get_sliced_data(df, 'r1_')
    selected_data = get_sliced_data(df, questionnaire_name)
    columns = selected_data.columns.values
    rm_missing_value(selected_data, missing_type=missing_type1, fix_value=0)
    # score_dict = score_dict_total['r1_']
    score_dict = score_dict_total[question_score_name]
    score_dict = form_score(score_dict)
    result_col = 'RESULT_' + question_score_name
    selected_data[result_col] = None
    selected_data[result_col] = df[result_col].map(lambda x: 0)
    for col in columns:
        if col!= result_col:
            selected_data[result_col]  = selected_data[result_col] + score_dict[get_question(col)]*selected_data[col]


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

# data file name
data_file = 'data/data_formal/orig/txt_file/merged_data/total_saved.txt'
save_file = 'data/data_formal/orig/txt_file/merged_data/total_computed.txt'
# score_dict_total
# score rules of each questionnaire
# 0 by default
score_dict_total = {'r1_':{0:[13,14,15],
                           1:list(range(1,13))},
                    'r2_':{0:[8,10,15,16,23],
                           1:clean_list(list(range(1,24)), refer_list=[8,10,15,16,23,2,3,4,6,9,13,19,20]),
                           -1:[2,3,4,6,9,13,19,20]},
                    'r3_':{1:list(range(1,25))},
                    'r4_FS': {1:[1,5,16,23,26],
                              -1:[7,12]},
                    'r4_EC': {1:[2,9,20,22],
                              -1:[4,14,18]},
                    'r4_PT': {1: [8, 11, 21, 25, 28],
                              -1: [3, 15]},
                    'r4_PD': {1: [6, 10, 17, 24, 27],
                              -1: [13, 19]},
                    'r5_Interdependent': {1:[1,2,4,6,9,10,11,13,18,20,23,24,27,28,30]},
                    'r5_Independent': {1:[3,5,7,8,12,14,15,16,17,19,21,22,25,26,29]},
                    'r6_altruism': {1:[4,10,12,16,23]},
                    'r7_':{1:clean_list(list(range(1,21)), refer_list=[1,3,4,6,7,10,13,14,16,19]),
                           -1:[1,3,4,6,7,10,13,14,16,19]},
                    'r8_':{1:list(range(1,22))}
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
    if type(value)==str or value<0 or value>99:
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
    index_t = selected_data.index.values
    rm_missing_value(selected_data, missing_type=missing_type1, fix_value=0)
    # score_dict = score_dict_total['r1_']
    score_dict = score_dict_total[question_score_name]
    score_dict = form_score(score_dict)
    result_col = 'RESULT_' + question_score_name
    selected_data[result_col] = None
    selected_data[result_col] = selected_data[result_col].map(lambda x: 0)
    for col in columns:
        if col!= result_col:
            selected_data[result_col]  = selected_data[result_col] + score_dict.setdefault(get_question(col),0)*selected_data[col]

    return pd.DataFrame(selected_data, columns=[result_col], index=index_t)

def main_decoder():
    file_name = data_file
    df = pd.read_csv(file_name, delimiter=',', header=0, index_col=0)
    df = df[~df.index.duplicated(keep='first')] # remove duplicated keys (important here! for the future join)
    index = df.index.values
    def lambda_sex(x):
        if str(x)=="\'男\'":
            return 0
        elif str(x)=="\'女\'":
            return 1
        return 1
    df['sex_response_new'] =  df['sex_response'].map(lambda x:lambda_sex(x))
    def lambda_age(x):
        try:
            value = int(str(x).replace('\'','').replace(' ','').replace('\t',''))
            return value
        except:
            return None
    df['age_response_new'] = df['age_response'].map(lambda x: lambda_age(x))
    result_df = pd.DataFrame(df, columns=['sex_response_new', 'age_response_new'], index=index)
    rm_missing_value(result_df,missing_type1,np.nan)

    # list_q = ['r1_', 'r2_']
    for q_score_name in score_dict_total:
        q_name = q_score_name.split('_')[0] + '_'
        tmp = compute_questionnaire(df, q_name, q_score_name)
        print('tmp:',tmp.values.shape)
        new_result_df = result_df.join(tmp)
        result_df = new_result_df
        print(q_name,q_score_name,new_result_df.values.shape)
    save_file_name = save_file
    result_df.to_csv(save_file_name)
    return result_df


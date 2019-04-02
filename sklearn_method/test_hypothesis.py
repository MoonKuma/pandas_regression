#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : test_hypothesis.py
# @Author  : MoonKuma
# @Date    : 2019/3/19
# @Desc   :  test hypothesis

from sklearn_method.prepare_hypothesis import prepare_hypothesis,prepare_hypothesis_on_erp
from sklearn_method.train_and_test import train_and_test
from sklearn_method.model_sets import *
import json
import os
import traceback

file_name = 'data/data_formal/result_final.txt'
save_path = 'data/result/model_result'
save_path_final = 'data/result/model_result/total_result'

# df, columns_dict_x, columns_dict_y = prepare_hypothesis(file_name=file_name)
df, columns_dict_x, columns_dict_y = prepare_hypothesis_on_erp(file_name=file_name)
# test one model and all hypothesis

def test_all_hypothesis(model_method=model_set_1):
    final_result_test = dict()
    final_result_train = dict()
    for feature_name in columns_dict_x.keys():
        x_columns = columns_dict_x[feature_name]
        for target_name in columns_dict_y.keys():
            y_column = columns_dict_y[target_name]
            hypothesis_name = feature_name + '_ON_' + target_name
            try:
                print('Testing hypothesis : ', hypothesis_name)
                result_test_dict, result_train_dict = train_and_test(df=df, x_columns=x_columns,
                                                                     y_column=y_column, model_method=model_method)
                final_result_test[hypothesis_name] = result_test_dict
                final_result_train[hypothesis_name] = result_train_dict
                _save_result_half_path(save_path, hypothesis_name, result_test_dict, result_train_dict)
            except:
                print('[ERROR] In testing', hypothesis_name)
                print(traceback.format_exc())
    _save_result_half_path(save_path_final, 'FINAL', final_result_test, final_result_train)
    return final_result_test,final_result_train


# test one hypothesis and all models
def test_all_models(test_times=1,model_method=model_set_simple):
    final_result_test = dict()
    final_result_train = dict()
    count_f = 0
    for feature_name in columns_dict_x.keys():
        count_f +=1
        if count_f>test_times:
            break
        count_t = 0
        x_columns = columns_dict_x[feature_name]
        for target_name in columns_dict_y.keys():
            count_t += 1
            if count_t > test_times:
                break
            y_column = columns_dict_y[target_name]
            hypothesis_name = feature_name + '_ON_' + target_name
            result_test_dict, result_train_dict = train_and_test(df=df, x_columns=x_columns,
                                                                 y_column=y_column, model_method=model_method)
            final_result_test[hypothesis_name] = result_test_dict
            final_result_train[hypothesis_name] = result_train_dict
    return final_result_test,final_result_train


# save result dict
def _save_result_half_path(save_path_loc, hypothesis, result_test, result_train):
    save_name_test = hypothesis + '_test.txt'
    save_name_train = hypothesis + '_train.txt'
    with open(os.path.join(save_path_loc, save_name_test), 'w') as file_test:
        j = json.dumps(result_test)
        file_test.write(j)
    with open(os.path.join(save_path_loc, save_name_train), 'w') as file_train:
        j = json.dumps(result_train)
        file_train.write(j)

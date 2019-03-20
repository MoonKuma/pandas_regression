#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : read_result.py
# @Author  : MoonKuma
# @Date    : 2019/3/20
# @Desc   : read template result data

import os
import json

result_path_f = 'data/model_set_result/'
report_path_f = 'data/report/'

# result_set = 'model_set_2_result'
def report(result_set):
    result_path = result_path_f + result_set
    report_file = report_path_f + result_set + '.txt'
    list_dir = os.listdir(result_path)

    result_test = dict()
    result_train = dict()

    for file_name in list_dir:
        file_op = os.path.join(result_path, file_name)
        with open(file_op) as f:
            json_obj = json.load(f)
            if file_name.endswith('test.txt'):
                result_test = json_obj
            else:
                result_train = json_obj

    features_list = list()
    target_list = list()
    model_list = list()

    # fulfill list
    for key in result_test.keys():
        key_array = key.split('_ON_')
        if key_array[0] not in features_list:
            features_list.append(key_array[0])
        if key_array[1] not in target_list:
            target_list.append(key_array[1])
        for model in result_test[key].keys():
            if model not in model_list:
                model_list.append(model)

    model_list = sorted(model_list)
    # test>0.5: o
    # test>0.1: +
    # train>0.5 and test<0.1: *
    # train<0.5 : -

    with open(report_file, 'w') as report:
        str2wri = str(model_list) + '\n'
        report.write(str2wri)
        for feature in features_list:
            for target in target_list:
                key = feature + '_ON_' + target
                str2wri = feature + ',' + target + ','
                if key in result_test.keys() and key in result_train.keys():
                    for model in model_list:
                        train = result_train[key].setdefault(model, 0)
                        test = result_test[key].setdefault(model, 0)
                        if test>0.5:
                            str2wri = str2wri + 'o'
                        elif test>0.1:
                            str2wri = str2wri + '+'
                        elif train>0.5 and test<=0.1:
                            str2wri = str2wri + '*'
                        elif train<=0.5:
                            str2wri = str2wri + '-'
                str2wri = str2wri + '\n'
                report.write(str2wri)




#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : read_result2.py
# @Author: MoonKuma
# @Date  : 2019/4/2
# @Desc  : another version of reading result

"""
- : <=0.2,
* : 0.2~0.5
o : >0.5
on train: report only selected method(eg:linear)
on test: report any findings
"""

import os
import json


default_path = ''
default_model_selected_train = ['linear']


def read_result2(result_path=default_path, model_select_train = default_model_selected_train):
    report_file = os.path.join(result_path,'result_report_total.txt')
    result_test = dict()
    result_train = dict()
    list_dir = os.listdir(result_path)
    for file_name in list_dir:
        if file_name == "FINAL_test.txt":
            result_test = _read_result_data(os.path.join(result_path, file_name))
        if file_name == "FINAL_train.txt":
            result_train = _read_result_data(os.path.join(result_path, file_name))
    # report here
    if len(result_test.keys()) <= 0 or len(result_train.keys()) <= 0:
        print('Missing data,len(result_test.keys())',len(result_test.keys()),'len(result_train.keys())',len(result_train.keys()))
        raise RuntimeError
    with open(report_file,'w') as file_report:
        features_list = list()
        target_list = list()
        model_list = list()

        # report test
        file_report.write('Test Result\n')
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

        splitter = ','
        header = [' '] + target_list
        str2wri = splitter.join(header) + '\n'
        file_report.write(str2wri)
        _write_in_detail(file_report, result_test, features_list, target_list, splitter, model_list)

        file_report.write('\n')
        file_report.write('\n')
        model_used = list()
        for model in model_list:
            if model in model_select_train:
                model_used.append(model)
        # report train
        if len(model_used) > 0:
            file_report.write('Train Result\n')
            splitter = ','
            header = [' '] + target_list
            str2wri = splitter.join(header) + '\n'
            file_report.write(str2wri)
            _write_in_detail(file_report, result_train, features_list, target_list, splitter, model_used)


def _read_result_data(result_file):
    with open(result_file) as f:
        json_obj = json.load(f)
        return json_obj


def _write_in_detail(file_report, result_data,features_list,target_list,splitter,model_list):
    for feature in features_list:
        data_report = [feature]
        for target in target_list:
            key = feature + '_ON_' + target
            str2wri = ''
            if key in result_data.keys():
                for model in model_list:
                    test = result_data[key].setdefault(model, 0)
                    if test > 0.5:
                        str2wri = str2wri + 'o'
                    elif test > 0.1:
                        str2wri = str2wri + '+'
                    else:
                        str2wri = str2wri + '-'
            data_report.append(str2wri)
        str2wri = splitter.join(data_report) + '\n'
        file_report.write(str2wri)
    file_report.write('\n')
    models = ['models'] + model_list
    str2wri = '|'.join(models) + '\n'
    file_report.write(str2wri)




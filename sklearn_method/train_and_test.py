#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : train_and_test.py
# @Author  : MoonKuma
# @Date    : 2019/3/18
# @Desc   : train certain data on certain model sets and test its results

from sklearn_method.model_sets import model_set_1
import pandas as pd
from sklearn_method.sklearn_method import create_sample,train_test

from sklearn.preprocessing import normalize


def train_and_test(df, x_columns, y_column, test_size = 0.1, test_times=10, model_method=model_set_1):
    """
    train and test on certain hypothesis with given machine leaning methods set
    :param df:  data frame
    :param x_columns:  feature columns
    :param y_column:  target column
    :param test_size:  test size ( for cross validation )
    :param test_times:  test times
    :param model_method:  machine learning models used, caution here the method name should be input here
    :return: result_test_dict, result_train_dict
    """
    # result
    result_test_dict = dict()
    result_train_dict = dict()
    data_copy_slice = pd.DataFrame(df, columns=x_columns + y_column) # no need for making copy
    data_drop_na = data_copy_slice.dropna(axis=0)
    # normalize Y
    data_drop_na[y_column] = normalize(data_drop_na[y_column], axis=0)
    # here try different times for i in range(0,test_times)
    model_dict = model_method()
    for i in range(0,test_times):
        sample = create_sample(data_drop_na, x_columns=x_columns, y_column=y_column, test_size=test_size)
        model_dict = model_method() # generate a new model each time
        for model_name in model_dict.keys():
            model = model_dict[model_name]
            train_score, test_score = train_test(sample=sample, model=model, model_name=model_name)
            result_test_dict[model_name] = result_test_dict.setdefault(model_name, 0) + test_score
            result_train_dict[model_name] = result_train_dict.setdefault(model_name, 0) + train_score
    for model_name in model_dict.keys():
        result_test_dict[model_name] = result_test_dict.setdefault(model_name, 0)/test_times
        result_train_dict[model_name] = result_train_dict.setdefault(model_name, 0)/test_times
        if result_test_dict[model_name] < 0:
            result_test_dict[model_name] = 0
    return result_test_dict, result_train_dict



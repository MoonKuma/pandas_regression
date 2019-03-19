#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : sklearn_method.py
# @Author  : MoonKuma
# @Date    : 2019/3/18
# @Desc   : some methods

import pandas as pd
from sklearn.model_selection import train_test_split
import time


def create_sample(df, x_columns, y_column, test_size=0.1):
    """
    Create a piece of sample
    :param df: data frame contains the target x/y columns
    :param x_columns: feature columns
    :param y_column: target column
    :param test_size: how much of data are left as test (default 0.1 i.e. 10%)
    :return: [X_train.values, X_test.values, y_train.values, y_test.values] for future training and testing
    """
    seed = int(time.time())%10000
    X_train, X_test, y_train, y_test = train_test_split(pd.DataFrame(df, columns=x_columns),
                                                        pd.DataFrame(df, columns=y_column), test_size=test_size, random_state=seed)
    return [X_train.values, X_test.values, y_train.values, y_test.values]

# train and test
def train_test(sample, model, model_name):
    """
    train and test with certain model
    :param sample: list contains [X_train, X_test, y_train, y_test], the same sample created by method 'create_sample'
    :param model: the model for testing
    :param model_name: name of model
    :return:score_train, score_test as score of train and test
    """
    start = time.time()
    msg = 'Start training model [' + str(model_name) + ']'
    print(msg)
    [X_train, X_test, y_train, y_test] = sample
    model.fit(X_train, (y_train*1.0).ravel())
    time_cost = time.time() - start
    score_train = model.score(X_train, (y_train*1.0).ravel())
    score_test = model.score(X_test, (y_test*1.0).ravel())
    msg = '[RESULT] Training model ['+ str(model_name) + '], with time cost [' + str(time_cost) + '], train score [' + str(score_train) +'], test score[' + str(score_test) + ']'
    print(msg)
    return score_train, score_test
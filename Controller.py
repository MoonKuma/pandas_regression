#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Controller.py
# @Author: MoonKuma
# @Date  : 2019/3/12
# @Desc  :

from pandas_method import compute_questionnaire,read_questionnaire
import pandas as pd
from sklearn_method.model_sets import *
from pandas_method import read_result

from sklearn_method.test_hypothesis import test_all_hypothesis,test_all_models

# read and compute questionnaire
# read_questionnaire.read_questionnaire()
# compute_questionnaire.main_decoder()
#
# train models
# from sklearn_method.test_hypothesis import test_all_hypothesis,test_all_models
# final_result_test, final_result_train = test_all_hypothesis()
final_result_test, final_result_train = test_all_hypothesis(model_method=model_set_3)
# final_result_test, final_result_train = test_all_hypothesis(model_method=model_set_3)

# report result
read_result.report(result_set = 'model_set_2_result')
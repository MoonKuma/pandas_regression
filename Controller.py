#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Controller.py
# @Author: MoonKuma
# @Date  : 2019/3/12
# @Desc  :

from pandas_method import compute_questionnaire,read_questionnaire
import pandas as pd

# read and compute questionnaire
read_questionnaire.read_questionnaire()
compute_questionnaire.main_decoder()
#
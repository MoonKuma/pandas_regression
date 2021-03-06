#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : model_sets.py
# @Author  : MoonKuma
# @Date    : 2019/3/17
# @Desc   : place to store model sets

from sklearn_method.sklearn_models import *

def model_set_simple():
    model_dict = dict()
    model_dict['linear'] = get_linear()
    return model_dict

def model_set_1():
    # standard regression models
    model_dict = dict()
    model_dict['linear'] = get_linear()
    model_dict['riged'] = get_riged()
    model_dict['lars'] = get_lars()
    model_dict['bayesian'] = get_bayesian()
    model_dict['svr_rbf'] = get_svm()
    model_dict['svr_linear'] = get_svm(kernel='linear')
    model_dict['svr_poly'] = get_svm(kernel='poly')
    model_dict['gaussian'] = get_gaussian()
    model_dict['kneighbors'] = get_kneighbors(n_neighbors=10)
    model_dict['random_forest'] = get_random_forest(max_depth=10, n_estimators=1000)
    model_dict['gradient_trees'] = get_gradient_trees(max_depth=10, n_estimators=1000)
    model_dict['neural_network'] = get_neural_network(hidden_layer_sizes=(50,25,10))
    return model_dict


def model_set_2():
    model_dict = dict()
    model_dict['linear'] = get_linear()
    model_dict['riged'] = get_riged(alpha=0.1)
    model_dict['random_forest'] = get_random_forest(max_depth=None, n_estimators=1000)
    return model_dict

def model_set_3():
    model_dict = dict()
    model_dict['linear'] = get_linear()
    model_dict['riged'] = get_riged()
    model_dict['bayesian'] = get_bayesian()
    model_dict['svr_rbf'] = get_svm()
    model_dict['svr_linear'] = get_svm(kernel='linear')
    model_dict['svr_poly'] = get_svm(kernel='poly')
    model_dict['random_forest'] = get_random_forest(max_depth=None, n_estimators=10000)
    model_dict['gradient_trees'] = get_gradient_trees(max_depth=None, n_estimators=10000)
    return model_dict

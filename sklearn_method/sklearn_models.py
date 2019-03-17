#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : sklearn_models.py
# @Author  : MoonKuma
# @Date    : 2019/3/17
# @Desc   :  sklearn models


from sklearn import linear_model
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn import neighbors
from sklearn import ensemble
from sklearn.neural_network import MLPRegressor

# general linear models
def get_linear():
    return linear_model.LinearRegression()


def get_riged(alpha=1.0):
    return linear_model.Ridge(alpha=alpha)


def get_lars(alpha=1.0):
    return linear_model.LassoLars(alpha=alpha)


def get_bayesian():
    return linear_model.BayesianRidge()


# kernel method models
def get_svm(kernel='rbf',C=1.0,gamma='auto_deprecated'):
    # kernel type: 'rbf', 'linear', 'poly'
    return svm.SVR(kernel=kernel, C=C, gamma=gamma)


def get_gaussian(kernel=None, alpha=1e-10):
    return GaussianProcessRegressor(kernel=kernel, alpha=alpha)


# Neighbors
def get_kneighbors(n_neighbors=5, weights = 'uniform'):
    return neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights)


# Ensembled methods
def get_random_forest(max_depth=3, n_estimators=100, max_features=1):
    return  ensemble.RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators, max_features=max_features)


def get_gradient_trees(n_estimators=100,max_depth=3, loss='ls'):
    return ensemble.GradientBoostingRegressor(n_estimators=n_estimators, max_depth=max_depth, loss=loss)


# Neural Network
def get_neural_network(hidden_layer_sizes=(100, ), activation='relu'):
    return MLPRegressor(hidden_layer_sizes=hidden_layer_sizes,activation=activation)



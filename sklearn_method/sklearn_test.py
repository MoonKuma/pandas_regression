#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sklearn_test.py
# @Author: MoonKuma
# @Date  : 2019/3/12
# @Desc  : test ski-learn method

from sklearn.svm import SVR
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_lin = SVR(kernel='linear', C=100, gamma='auto')
svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,
               coef0=1)



from sklearn.ensemble import GradientBoostingRegressor

est = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,max_depth=1, random_state=0, loss='ls')


from sklearn.neural_network import MLPRegressor

clf = MLPRegressor(hidden_layer_sizes=(100, ),
                   activation='relu', solver='adam', alpha=0.0001, batch_size='auto',
                   learning_rate='constant', learning_rate_init=0.001, power_t=0.5,
                   max_iter=200, shuffle=True, random_state=None,
                   tol=0.0001, verbose=False, warm_start=False, momentum=0.9,
                   nesterovs_momentum=True, early_stopping=False,
                   validation_fraction=0.1, beta_1=0.9, beta_2=0.999,
                   epsilon=1e-08, n_iter_no_change=10)


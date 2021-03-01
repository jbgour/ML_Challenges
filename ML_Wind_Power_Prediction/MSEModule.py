# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:24:03 2019

@author: JBG
"""

from sklearn.metrics import mean_squared_error

def MSE(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)


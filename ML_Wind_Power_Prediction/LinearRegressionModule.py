# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:32:07 2019

@author: JBG
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def linearRegression(trainSet, trainLabels, testSet):
    clf = linear_model.LinearRegression()
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict(testSet)
    return predictedLabels
    
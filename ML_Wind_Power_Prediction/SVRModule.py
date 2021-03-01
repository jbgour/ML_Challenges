# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:58:25 2019

@author: JBG
"""

from sklearn.svm import SVR
import numpy as np

def SVRFunction(trainSet, trainLabels, testSet):
    np.random.seed(0)
    clf = SVR(gamma='scale', C=1.0, epsilon=0.2)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict(testSet)
    return predictedLabels
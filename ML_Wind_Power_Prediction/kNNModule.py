# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:00:03 2018

@author: JBG
"""

from sklearn.neighbors import KNeighborsRegressor


def kNN(trainSet, trainLabels, testSet):
    clf = KNeighborsRegressor(n_neighbors=100)
    clf.fit(trainSet, trainLabels.ravel())
    predictedLabels = clf.predict(testSet)
    return predictedLabels
